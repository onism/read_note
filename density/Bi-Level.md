# bilevel optimization

Bilevel optimization is defined as a mathmatical program, where an optimization problem contains another optimiazation problem as a constraint.

## General formulation and definitions

For the upper-level objective function $F$ and lower level objective function f, the bilevel problem is given by

$$
\min_{x_u \in X_u, x_l \in X_{L}} F(x_u,x_l)
$$
subject to
 

\[
  \begin{aligned} 
  & x_l \in \arg \min_{x_l \in X_L}\{f(x_u,x_l) : g_j(x_u, x_l) \leq 0, j=1...J \}  \\
   &   G_k(x_u,x_l) \leq 0,k=1,...,K  
  \end{aligned}
\]

where $G_k$ denote the uppder level constraints and $g_j$ represent the lower level constraints, respectively.


A simple example from pyomo



    from pyomo.environ import *
    from pyomo.bilevel import *

    def pyomo_create_model(options, model_options):
        M = ConcreteModel()
        M.x = Var(bounds=(0,None))
        M.y1 = Var(bounds=(1,None))
        M.y2 = Var(bounds=(None,2))
        M.y3 = Var(bounds=(None,None))
        M.y4 = Var(bounds=(3,4))
        M.o = Objective(expr=M.x - 4*M.y1)

        M.sub = SubModel(fixed=M.x)
        M.sub.o  = Objective( expr=                     + M.y2 +  9*M.y3      )
        M.sub.c1 = Constraint(expr=        M.x + 5*M.y1        + 10*M.y3 <= 19)
        M.sub.c2 = Constraint(expr=20 <= 2*M.x + 6*M.y1                       )
        M.sub.c3 = Constraint(expr=21 <= 3*M.x + 7*M.y1                  <= 21)
        M.sub.c4 = Constraint(expr=22 == 4*M.x + 8*M.y1                       )

        return M

    instance = pyomo_create_model(None, None)
    xfrm = TransformationFactory('bilevel.linear_mpec')
    xfrm.apply_to(instance)
    instance.pprint()

The output:


    5 Var Declarations
    x : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :  None :  None : False :  True :  Reals
    y1 : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     1 :  None :  None : False :  True :  Reals
    y2 : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :  None :  None :     2 : False :  True :  Reals
    y3 : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :  None :  None :  None : False :  True :  Reals
    y4 : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     3 :  None :     4 : False :  True :  Reals

    1 Objective Declarations
        o : Size=1, Index=None, Active=True
            Key  : Active : Sense    : Expression
            None :   True : minimize : x - 4*y1

    2 Block Declarations
        sub : Size=1, Index=None, Active=True
            1 Objective Declarations
                o : Size=1, Index=None, Active=False
                    Key  : Active : Sense    : Expression
                    None :  False : minimize : y2 + 9*y3

        4 Constraint Declarations
            c1 : Size=1, Index=None, Active=False
                Key  : Lower : Body             : Upper : Active
                None :  -Inf : x + 5*y1 + 10*y3 :  19.0 :  False
            c2 : Size=1, Index=None, Active=False
                Key  : Lower : Body       : Upper : Active
                None :  20.0 : 2*x + 6*y1 :  +Inf :  False
            c3 : Size=1, Index=None, Active=False
                Key  : Lower : Body       : Upper : Active
                None :  21.0 : 3*x + 7*y1 :  21.0 :  False
            c4 : Size=1, Index=None, Active=False
                Key  : Lower : Body       : Upper : Active
                None :  22.0 : 4*x + 8*y1 :  22.0 :  False

        5 Declarations: o c1 c2 c3 c4
    sub_kkt : Size=1, Index=None, Active=True
        5 Set Declarations
            c1_index : Dim=0, Dimen=1, Size=4, Domain=None, Ordered=False, Bounds=None
                [1, 2, 3, 4]
            c2_index : Dim=0, Dimen=1, Size=2, Domain=None, Ordered=False, Bounds=None
                [1, 2]
            c3_index : Dim=0, Dimen=1, Size=4, Domain=None, Ordered=False, Bounds=None
                [1, 2, 3, 4]
            u_index : Dim=0, Dimen=1, Size=4, Domain=None, Ordered=False, Bounds=None
                [1, 2, 3, 4]
            v_index : Dim=0, Dimen=1, Size=4, Domain=None, Ordered=False, Bounds=None
                [1, 2, 3, 4]

        2 Var Declarations
            u : Size=4, Index=sub_kkt.u_index
                Key : Lower : Value : Upper : Fixed : Stale : Domain
                  1 :  None :  None :  None : False :  True :  Reals
                  2 :  None :  None :  None : False :  True :  Reals
                  3 :  None :  None :  None : False :  True :  Reals
                  4 :  None :  None :  None : False :  True :  Reals
            v : Size=4, Index=sub_kkt.v_index
                Key : Lower : Value : Upper : Fixed : Stale : Domain
                  1 :  None :  None :  None : False :  True :  Reals
                  2 :  None :  None :  None : False :  True :  Reals
                  3 :  None :  None :  None : False :  True :  Reals
                  4 :  None :  None :  None : False :  True :  Reals

        1 Constraint Declarations
            c1 : Size=4, Index=sub_kkt.c1_index, Active=True
                Key : Lower : Body                                                                                : Upper : Active
                  1 :   0.0 :                                                                    1 + sub_kkt.v[2] :   0.0 :   True
                  2 :   0.0 :                                                                 9 + 10*sub_kkt.u[1] :   0.0 :   True
                  3 :   0.0 :  - sub_kkt.v[1] + 5*sub_kkt.u[1] - 6*sub_kkt.u[2] + 8*sub_kkt.u[4] + 7*sub_kkt.u[3] :   0.0 :   True
                  4 :   0.0 :                                                       - sub_kkt.v[3] + sub_kkt.v[4] :   0.0 :   True

        2 Complementarity Declarations
            c2 : Size=2, Index=sub_kkt.c2_index, Active=True
                Key : Arg0                       : Arg1                  : Active
                  1 : x + 5*y1 + 10*y3  <=  19.0 : 0.0  <=  sub_kkt.u[1] :   True
                  2 :    - 2*x - 6*y1  <=  -20.0 : 0.0  <=  sub_kkt.u[2] :   True
            c3 : Size=4, Index=sub_kkt.c3_index, Active=True
                Key : Arg0        : Arg1                  : Active
                  1 : 1.0  <=  y1 : 0.0  <=  sub_kkt.v[1] :   True
                  2 : y2  <=  2.0 : 0.0  <=  sub_kkt.v[2] :   True
                  3 : 3.0  <=  y4 : 0.0  <=  sub_kkt.v[3] :   True
                  4 : y4  <=  4.0 : 0.0  <=  sub_kkt.v[4] :   True

        10 Declarations: u_index u v_index v c1_index c1 c2_index c2 c3_index c3

    8 Declarations: x y1 y2 y3 y4 o sub sub_kkt