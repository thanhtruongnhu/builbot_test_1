# Copyright (C) 2015 Akselos


from main import test_fe_solver
import argparse

print("START FE SOLVER STABILITY TEST")
parser = argparse.ArgumentParser()
# parser.add_argument("aks_filename")
# parser.add_argument("reference_solution_exo_filename")
parser.add_argument("--mesh-stitching-tolerance", type=float, default=0.5)
parser.add_argument("--tolerance", type=float, default=1e-6)
parser.add_argument("--num-cores", type=int, default=1)
parser.add_argument("--use-elem-stress", default=False, action='store_true')
# The --von-mises-stress-only flag skips writing stress/strain components and instead
# just computes and writes the Von Mises stress, which can be useful for testing
# stresses without writing quite so much data.
parser.add_argument("--von-mises-stress-only", default=False, action='store_true')
parser.add_argument("--use-global-coords-for-surface-constraints", default=False, action='store_true')
parser.add_argument("--is-shell", default=False, action='store_true')
parser.add_argument("--do-not-compare-exo-files", default=False, action='store_true')
parser.add_argument("--solve-type", type=str, default='default')
parser.add_argument("--contact-algorithm", type=str, default='Augmented Lagrangian')
parser.add_argument("--finite-sliding", action='store_true', default=False)
parser.add_argument("--uncoupled-submodel-solve", default=False, action='store_true')
parser.add_argument("--submodel-ids", nargs='+', type=int)
parser.add_argument("--time-parameters", nargs='+', type=float)
parser.add_argument("--max-dofs-per-port", type=int, default=-1)
parser.add_argument("--allow-nonconforming-port-meshes", action='store_true', default=False)
parser.add_argument("--use-reduced-integration", action='store_true', default=False)
parser.add_argument("--use-parallel-mesh-stitching", action='store_true', default=False)
parser.add_argument("--ref_x", type=float)
parser.add_argument("--ref_y", type=float)
parser.add_argument("--ref_z", type=float)
parser.add_argument("--ref_xy", type=float, default=0.0)
parser.add_argument("--ref_xz", type=float, default=0.0)
parser.add_argument("--ref_yz", type=float, default=0.0)
parser.add_argument("--origin_x", type=float, default=0.0)
parser.add_argument("--origin_y", type=float, default=0.0)
parser.add_argument("--origin_z", type=float, default=0.0)
parser.add_argument("--force_moment_test_type", type=str)
parser.add_argument("--ref_units", type=str)
parser.add_argument("--skip-precomputed-interface-functions", action='store_true', default=False)
parser.add_argument("--include-materials-in-plot", action='store_true', default=False)
parser.add_argument("--compare-component-solutions", action='store_true', default=False)
parser.add_argument("--do-not-use-component-datasets", action='store_true', default=False)

args = parser.parse_args()
args.aks_filename = "hemisphere.aks"
args.reference_solution_exo_filename = "hemisphere.exo"
args.is_shell = True

# test_fe_solver(os.path.abspath("aks_files/" + args.aks_filename),
test_fe_solver(os.path.abspath("worker/aks_files/" + args.aks_filename),
               args.reference_solution_exo_filename,
               args.num_cores,
               args.mesh_stitching_tolerance,
               args.tolerance,
               args.use_elem_stress,
               args.von_mises_stress_only,
               args.use_global_coords_for_surface_constraints,
               args.is_shell,
               args.do_not_compare_exo_files,
               args.solve_type,
               args.uncoupled_submodel_solve,
               args.submodel_ids,
               args.time_parameters,
               args.contact_algorithm,
               args.finite_sliding,
               args.ref_x, args.ref_y, args.ref_z,
               args.ref_xy, args.ref_xz, args.ref_yz,
               args.origin_x, args.origin_y, args.origin_z,
               args.force_moment_test_type, args.ref_units,
               args.skip_precomputed_interface_functions,
               args.include_materials_in_plot,
               args.max_dofs_per_port,
               allow_nonconforming_port_meshes=args.allow_nonconforming_port_meshes,
               use_reduced_integration=args.use_reduced_integration,
               use_parallel_mesh_stitching=args.use_parallel_mesh_stitching,
               compare_component_solutions=args.compare_component_solutions,
               do_not_use_component_datasets=args.do_not_use_component_datasets)
print("FINISH !")