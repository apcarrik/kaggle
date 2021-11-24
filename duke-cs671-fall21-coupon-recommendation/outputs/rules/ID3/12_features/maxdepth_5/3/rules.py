def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4716, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5887, "metric_value": 0.4562, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Distance", "instances": 3057, "metric_value": 0.4852, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Passanger", "instances": 2765, "metric_value": 0.4824, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 1675, "metric_value": 0.4929, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Gender", "instances": 1620, "metric_value": 0.4952, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Occupation", "instances": 811, "metric_value": 0.486, "depth": 7}
							if obj[6]<=20.215819106797763:
								# {"feature": "Age", "instances": 750, "metric_value": 0.4915, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Bar", "instances": 721, "metric_value": 0.4908, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Education", "instances": 514, "metric_value": 0.4839, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Time", "instances": 486, "metric_value": 0.4896, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 288, "metric_value": 0.4884, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 198, "metric_value": 0.4812, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>3:
											# {"feature": "Direction_same", "instances": 28, "metric_value": 0.352, "depth": 11}
											if obj[10]>0:
												# {"feature": "Time", "instances": 14, "metric_value": 0.4167, "depth": 12}
												if obj[1]>0:
													return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												# {"feature": "Time", "instances": 14, "metric_value": 0.2251, "depth": 12}
												if obj[1]>0:
													return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Education", "instances": 207, "metric_value": 0.4921, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Time", "instances": 201, "metric_value": 0.4933, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Direction_same", "instances": 135, "metric_value": 0.4918, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Direction_same", "instances": 66, "metric_value": 0.4935, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>3:
											# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>6:
									# {"feature": "Time", "instances": 29, "metric_value": 0.4269, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Bar", "instances": 25, "metric_value": 0.4229, "depth": 10}
										if obj[7]<=1.0:
											# {"feature": "Education", "instances": 21, "metric_value": 0.3985, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.3872, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>1.0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>3:
										# {"feature": "Bar", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[7]<=0.0:
											return 'True'
										elif obj[7]>0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[6]>20.215819106797763:
								# {"feature": "Education", "instances": 61, "metric_value": 0.3301, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Direction_same", "instances": 47, "metric_value": 0.2684, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Time", "instances": 30, "metric_value": 0.3228, "depth": 10}
										if obj[1]>1:
											# {"feature": "Age", "instances": 17, "metric_value": 0.1882, "depth": 11}
											if obj[4]>2:
												# {"feature": "Bar", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[7]<=0.0:
													return 'True'
												elif obj[7]>0.0:
													return 'True'
												else: return 'True'
											elif obj[4]<=2:
												return 'True'
											else: return 'True'
										elif obj[1]<=1:
											# {"feature": "Age", "instances": 13, "metric_value": 0.4103, "depth": 11}
											if obj[4]<=3:
												# {"feature": "Bar", "instances": 12, "metric_value": 0.4167, "depth": 12}
												if obj[7]<=1.0:
													return 'True'
												elif obj[7]>1.0:
													return 'False'
												else: return 'False'
											elif obj[4]>3:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[10]>0:
										# {"feature": "Time", "instances": 17, "metric_value": 0.0784, "depth": 10}
										if obj[1]<=1:
											return 'True'
										elif obj[1]>1:
											# {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[4]>1:
												return 'True'
											elif obj[4]<=1:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[5]>2:
									# {"feature": "Time", "instances": 14, "metric_value": 0.2286, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Age", "instances": 10, "metric_value": 0.24, "depth": 10}
										if obj[4]>0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[10]>0:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[7]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[3]>0:
							# {"feature": "Bar", "instances": 809, "metric_value": 0.4961, "depth": 7}
							if obj[7]>-1.0:
								# {"feature": "Time", "instances": 800, "metric_value": 0.4977, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 516, "metric_value": 0.4958, "depth": 9}
									if obj[10]>0:
										# {"feature": "Occupation", "instances": 280, "metric_value": 0.4897, "depth": 10}
										if obj[6]>4:
											# {"feature": "Education", "instances": 167, "metric_value": 0.4763, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Age", "instances": 134, "metric_value": 0.4653, "depth": 12}
												if obj[4]<=4:
													return 'True'
												elif obj[4]>4:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												# {"feature": "Age", "instances": 33, "metric_value": 0.4909, "depth": 12}
												if obj[4]>1:
													return 'True'
												elif obj[4]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]<=4:
											# {"feature": "Age", "instances": 113, "metric_value": 0.4934, "depth": 11}
											if obj[4]>0:
												# {"feature": "Education", "instances": 95, "metric_value": 0.4892, "depth": 12}
												if obj[5]>1:
													return 'False'
												elif obj[5]<=1:
													return 'True'
												else: return 'True'
											elif obj[4]<=0:
												# {"feature": "Education", "instances": 18, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=1:
													return 'True'
												elif obj[5]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]<=0:
										# {"feature": "Occupation", "instances": 236, "metric_value": 0.4851, "depth": 10}
										if obj[6]<=21:
											# {"feature": "Age", "instances": 227, "metric_value": 0.4942, "depth": 11}
											if obj[4]>0:
												# {"feature": "Education", "instances": 181, "metric_value": 0.4944, "depth": 12}
												if obj[5]>0:
													return 'False'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]<=0:
												# {"feature": "Education", "instances": 46, "metric_value": 0.4551, "depth": 12}
												if obj[5]<=1:
													return 'False'
												elif obj[5]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>21:
											# {"feature": "Education", "instances": 9, "metric_value": 0.1667, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												# {"feature": "Age", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[4]>2:
													return 'False'
												elif obj[4]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>1:
									# {"feature": "Occupation", "instances": 284, "metric_value": 0.4819, "depth": 9}
									if obj[6]<=13:
										# {"feature": "Age", "instances": 231, "metric_value": 0.477, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Education", "instances": 223, "metric_value": 0.48, "depth": 11}
											if obj[5]>1:
												# {"feature": "Direction_same", "instances": 117, "metric_value": 0.4974, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[5]<=1:
												# {"feature": "Direction_same", "instances": 106, "metric_value": 0.4596, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>6:
											# {"feature": "Education", "instances": 8, "metric_value": 0.125, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>13:
										# {"feature": "Age", "instances": 53, "metric_value": 0.4297, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Education", "instances": 47, "metric_value": 0.411, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 36, "metric_value": 0.4499, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>2:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1558, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[7]<=-1.0:
								# {"feature": "Time", "instances": 9, "metric_value": 0.1667, "depth": 8}
								if obj[1]>1:
									return 'False'
								elif obj[1]<=1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[10]>0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]>2.0:
						# {"feature": "Time", "instances": 55, "metric_value": 0.3433, "depth": 6}
						if obj[1]>0:
							# {"feature": "Age", "instances": 43, "metric_value": 0.3929, "depth": 7}
							if obj[4]>0:
								# {"feature": "Occupation", "instances": 28, "metric_value": 0.317, "depth": 8}
								if obj[6]<=6:
									# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3975, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Education", "instances": 11, "metric_value": 0.4481, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[7]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>3:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[7]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[5]<=3:
											return 'True'
										elif obj[5]>3:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>6:
									# {"feature": "Gender", "instances": 11, "metric_value": 0.1515, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[5]<=4:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[7]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								# {"feature": "Gender", "instances": 15, "metric_value": 0.3143, "depth": 8}
								if obj[3]>0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.3571, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Occupation", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[7]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=18:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Age", "instances": 1090, "metric_value": 0.4589, "depth": 5}
					if obj[4]>1:
						# {"feature": "Bar", "instances": 692, "metric_value": 0.4712, "depth": 6}
						if obj[7]<=2.0:
							# {"feature": "Occupation", "instances": 651, "metric_value": 0.469, "depth": 7}
							if obj[6]<=13.852614400462308:
								# {"feature": "Time", "instances": 550, "metric_value": 0.4754, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Restaurant20to50", "instances": 337, "metric_value": 0.4817, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Education", "instances": 267, "metric_value": 0.4864, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Gender", "instances": 244, "metric_value": 0.4958, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 123, "metric_value": 0.4973, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 121, "metric_value": 0.4942, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>3:
											# {"feature": "Gender", "instances": 23, "metric_value": 0.3794, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Education", "instances": 70, "metric_value": 0.431, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Gender", "instances": 67, "metric_value": 0.4246, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 39, "metric_value": 0.4602, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>3:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Education", "instances": 213, "metric_value": 0.4513, "depth": 9}
									if obj[5]<=1:
										# {"feature": "Gender", "instances": 111, "metric_value": 0.4122, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.3616, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 47, "metric_value": 0.4002, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 54, "metric_value": 0.4544, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 47, "metric_value": 0.4491, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>1:
										# {"feature": "Gender", "instances": 102, "metric_value": 0.4739, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 54, "metric_value": 0.49, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 50, "metric_value": 0.4992, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.4283, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 33, "metric_value": 0.3967, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>13.852614400462308:
								# {"feature": "Education", "instances": 101, "metric_value": 0.4013, "depth": 8}
								if obj[5]>0:
									# {"feature": "Gender", "instances": 57, "metric_value": 0.4602, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.3393, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Time", "instances": 25, "metric_value": 0.3111, "depth": 11}
											if obj[1]>2:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=2:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Time", "instances": 7, "metric_value": 0.3714, "depth": 11}
											if obj[1]>2:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=2:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4255, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Time", "instances": 22, "metric_value": 0.4636, "depth": 11}
											if obj[1]>2:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=2:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]<=0:
									# {"feature": "Time", "instances": 44, "metric_value": 0.2902, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.3359, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 24, "metric_value": 0.3739, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3599, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.2083, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>3:
										# {"feature": "Gender", "instances": 12, "metric_value": 0.1458, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.2143, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>2.0:
							# {"feature": "Occupation", "instances": 41, "metric_value": 0.4378, "depth": 7}
							if obj[6]>2:
								# {"feature": "Time", "instances": 39, "metric_value": 0.4438, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Gender", "instances": 26, "metric_value": 0.4773, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 22, "metric_value": 0.4935, "depth": 10}
										if obj[5]>1:
											# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.4898, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]<=1:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.4286, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Education", "instances": 13, "metric_value": 0.3077, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=1:
						# {"feature": "Time", "instances": 398, "metric_value": 0.4216, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Restaurant20to50", "instances": 219, "metric_value": 0.4532, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Occupation", "instances": 166, "metric_value": 0.4707, "depth": 8}
								if obj[6]<=20:
									# {"feature": "Bar", "instances": 157, "metric_value": 0.475, "depth": 9}
									if obj[7]>-1.0:
										# {"feature": "Education", "instances": 150, "metric_value": 0.4722, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Gender", "instances": 136, "metric_value": 0.4774, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 80, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 56, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>3:
											# {"feature": "Gender", "instances": 14, "metric_value": 0.3937, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=-1.0:
										# {"feature": "Education", "instances": 7, "metric_value": 0.3429, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>20:
									# {"feature": "Education", "instances": 9, "metric_value": 0.2963, "depth": 9}
									if obj[5]>0:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]>1.0:
								# {"feature": "Bar", "instances": 53, "metric_value": 0.3608, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Education", "instances": 27, "metric_value": 0.2399, "depth": 9}
									if obj[5]>0:
										# {"feature": "Occupation", "instances": 21, "metric_value": 0.3031, "depth": 10}
										if obj[6]>1:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.3538, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.2188, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									# {"feature": "Education", "instances": 26, "metric_value": 0.4487, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Occupation", "instances": 24, "metric_value": 0.4614, "depth": 10}
										if obj[6]<=12:
											# {"feature": "Gender", "instances": 19, "metric_value": 0.4985, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4983, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>12:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>3:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Occupation", "instances": 179, "metric_value": 0.3691, "depth": 7}
							if obj[6]<=7.189944134078212:
								# {"feature": "Bar", "instances": 116, "metric_value": 0.3172, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 115, "metric_value": 0.315, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Education", "instances": 82, "metric_value": 0.3517, "depth": 10}
										if obj[5]>1:
											# {"feature": "Gender", "instances": 48, "metric_value": 0.3853, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 35, "metric_value": 0.3527, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4734, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=1:
											# {"feature": "Gender", "instances": 34, "metric_value": 0.2858, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.3299, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										# {"feature": "Education", "instances": 33, "metric_value": 0.2027, "depth": 10}
										if obj[5]>0:
											# {"feature": "Gender", "instances": 18, "metric_value": 0.0926, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.28, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[6]>7.189944134078212:
								# {"feature": "Bar", "instances": 63, "metric_value": 0.4194, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Education", "instances": 48, "metric_value": 0.3692, "depth": 9}
									if obj[5]>1:
										# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.4495, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Gender", "instances": 30, "metric_value": 0.4622, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=1:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.1877, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 14, "metric_value": 0.125, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									# {"feature": "Education", "instances": 15, "metric_value": 0.28, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.3, "depth": 10}
										if obj[9]<=0.0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>0.0:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[11]>2:
				# {"feature": "Time", "instances": 292, "metric_value": 0.4475, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 244, "metric_value": 0.479, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Bar", "instances": 196, "metric_value": 0.4678, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Occupation", "instances": 99, "metric_value": 0.4188, "depth": 7}
							if obj[6]>1:
								# {"feature": "Age", "instances": 87, "metric_value": 0.3784, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.2726, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Gender", "instances": 31, "metric_value": 0.1746, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 19, "metric_value": 0.1884, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.1884, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Passanger", "instances": 12, "metric_value": 0.1528, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.1528, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										# {"feature": "Gender", "instances": 19, "metric_value": 0.3972, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 12, "metric_value": 0.4861, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Passanger", "instances": 7, "metric_value": 0.2449, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>3:
									# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.4787, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Gender", "instances": 24, "metric_value": 0.4622, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 17, "metric_value": 0.4844, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4844, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Passanger", "instances": 7, "metric_value": 0.4082, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										# {"feature": "Gender", "instances": 13, "metric_value": 0.4945, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]<=1:
								# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.35, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.3667, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>1:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[9]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]<=0.0:
							# {"feature": "Age", "instances": 97, "metric_value": 0.461, "depth": 7}
							if obj[4]<=5:
								# {"feature": "Occupation", "instances": 80, "metric_value": 0.4795, "depth": 8}
								if obj[6]<=7:
									# {"feature": "Gender", "instances": 49, "metric_value": 0.4343, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.2714, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Passanger", "instances": 19, "metric_value": 0.1884, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.1884, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.4688, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.4755, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Passanger", "instances": 13, "metric_value": 0.497, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Passanger", "instances": 9, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>7:
									# {"feature": "Gender", "instances": 31, "metric_value": 0.4731, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4667, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Passanger", "instances": 15, "metric_value": 0.4978, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.3077, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Passanger", "instances": 13, "metric_value": 0.355, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[4]>5:
								# {"feature": "Occupation", "instances": 17, "metric_value": 0.2059, "depth": 8}
								if obj[6]<=9:
									# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.2136, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Gender", "instances": 11, "metric_value": 0.1364, "depth": 10}
										if obj[3]<=0:
											return 'False'
										elif obj[3]>0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>9:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Gender", "instances": 48, "metric_value": 0.4491, "depth": 6}
						if obj[3]>0:
							# {"feature": "Age", "instances": 25, "metric_value": 0.3088, "depth": 7}
							if obj[4]>1:
								# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.1871, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Bar", "instances": 18, "metric_value": 0.1852, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "Occupation", "instances": 12, "metric_value": 0.2593, "depth": 10}
										if obj[6]<=4:
											# {"feature": "Passanger", "instances": 9, "metric_value": 0.1975, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>4:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>0.0:
										return 'True'
									else: return 'True'
								elif obj[9]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[4]<=1:
								# {"feature": "Occupation", "instances": 6, "metric_value": 0.2667, "depth": 8}
								if obj[6]<=13:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.3, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=0.0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>0.0:
											return 'False'
										else: return 'False'
									elif obj[7]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[6]>13:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 23, "metric_value": 0.4174, "depth": 7}
							if obj[6]<=21:
								# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.4188, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Age", "instances": 16, "metric_value": 0.3846, "depth": 9}
									if obj[4]>2:
										# {"feature": "Bar", "instances": 13, "metric_value": 0.4487, "depth": 10}
										if obj[7]<=1.0:
											# {"feature": "Passanger", "instances": 12, "metric_value": 0.4861, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>1.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=2:
										return 'False'
									else: return 'False'
								elif obj[9]>2.0:
									# {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[4]<=3:
										return 'True'
									elif obj[4]>3:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>21:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 48, "metric_value": 0.0357, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Age", "instances": 7, "metric_value": 0.0, "depth": 6}
						if obj[4]<=5:
							return 'True'
						elif obj[4]>5:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			# {"feature": "Distance", "instances": 2830, "metric_value": 0.4095, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Passanger", "instances": 2559, "metric_value": 0.3976, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1657, "metric_value": 0.4189, "depth": 5}
					if obj[6]<=18.149362003525606:
						# {"feature": "Age", "instances": 1539, "metric_value": 0.4258, "depth": 6}
						if obj[4]>0:
							# {"feature": "Time", "instances": 1328, "metric_value": 0.4163, "depth": 7}
							if obj[1]>0:
								# {"feature": "Gender", "instances": 941, "metric_value": 0.4296, "depth": 8}
								if obj[3]>0:
									# {"feature": "Education", "instances": 503, "metric_value": 0.4512, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Bar", "instances": 484, "metric_value": 0.4464, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Restaurant20to50", "instances": 293, "metric_value": 0.4658, "depth": 11}
											if obj[9]<=3.0:
												# {"feature": "Direction_same", "instances": 281, "metric_value": 0.4644, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[9]>3.0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4857, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=0.0:
											# {"feature": "Restaurant20to50", "instances": 191, "metric_value": 0.4001, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Direction_same", "instances": 173, "metric_value": 0.3904, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4618, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[5]>3:
										# {"feature": "Bar", "instances": 19, "metric_value": 0.3947, "depth": 10}
										if obj[7]<=0.0:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4583, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4722, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Bar", "instances": 438, "metric_value": 0.4002, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 238, "metric_value": 0.3742, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Education", "instances": 166, "metric_value": 0.3993, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Direction_same", "instances": 155, "metric_value": 0.4054, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>3:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2727, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Direction_same", "instances": 72, "metric_value": 0.3102, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Education", "instances": 48, "metric_value": 0.2762, "depth": 12}
												if obj[5]>0:
													return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Education", "instances": 24, "metric_value": 0.3571, "depth": 12}
												if obj[5]<=2:
													return 'True'
												elif obj[5]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Education", "instances": 200, "metric_value": 0.426, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Restaurant20to50", "instances": 180, "metric_value": 0.4149, "depth": 11}
											if obj[9]<=3.0:
												# {"feature": "Direction_same", "instances": 175, "metric_value": 0.4263, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[9]>3.0:
												return 'True'
											else: return 'True'
										elif obj[5]>3:
											# {"feature": "Direction_same", "instances": 20, "metric_value": 0.4484, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3916, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[9]<=3.0:
													return 'True'
												elif obj[9]>3.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 387, "metric_value": 0.3679, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Bar", "instances": 239, "metric_value": 0.422, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Restaurant20to50", "instances": 162, "metric_value": 0.4494, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Gender", "instances": 160, "metric_value": 0.4526, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 85, "metric_value": 0.4269, "depth": 12}
												if obj[5]<=2:
													return 'True'
												elif obj[5]>2:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 75, "metric_value": 0.4695, "depth": 12}
												if obj[5]<=2:
													return 'True'
												elif obj[5]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Education", "instances": 77, "metric_value": 0.347, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Gender", "instances": 39, "metric_value": 0.4154, "depth": 11}
											if obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.3636, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4769, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>1:
											# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.2505, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Gender", "instances": 29, "metric_value": 0.3273, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]>0:
									# {"feature": "Restaurant20to50", "instances": 148, "metric_value": 0.2625, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Bar", "instances": 126, "metric_value": 0.2939, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Education", "instances": 105, "metric_value": 0.253, "depth": 11}
											if obj[5]>1:
												# {"feature": "Gender", "instances": 57, "metric_value": 0.1866, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												# {"feature": "Gender", "instances": 48, "metric_value": 0.316, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											# {"feature": "Education", "instances": 21, "metric_value": 0.4512, "depth": 11}
											if obj[5]>1:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.4688, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Education", "instances": 211, "metric_value": 0.4526, "depth": 7}
							if obj[5]<=3:
								# {"feature": "Restaurant20to50", "instances": 184, "metric_value": 0.4785, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Bar", "instances": 148, "metric_value": 0.4591, "depth": 9}
									if obj[7]<=3.0:
										# {"feature": "Gender", "instances": 140, "metric_value": 0.4615, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 101, "metric_value": 0.4462, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Time", "instances": 61, "metric_value": 0.4668, "depth": 12}
												if obj[1]<=3:
													return 'True'
												elif obj[1]>3:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Time", "instances": 40, "metric_value": 0.3982, "depth": 12}
												if obj[1]>0:
													return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 39, "metric_value": 0.4611, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Direction_same", "instances": 27, "metric_value": 0.4828, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.3704, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>3.0:
										return 'True'
									else: return 'True'
								elif obj[9]>2.0:
									# {"feature": "Gender", "instances": 36, "metric_value": 0.4021, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Bar", "instances": 20, "metric_value": 0.3733, "depth": 10}
										if obj[7]>1.0:
											# {"feature": "Time", "instances": 15, "metric_value": 0.3643, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.1905, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=1.0:
											# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[1]>1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Bar", "instances": 16, "metric_value": 0.2625, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Time", "instances": 10, "metric_value": 0.3667, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>3:
								# {"feature": "Gender", "instances": 27, "metric_value": 0.1852, "depth": 8}
								if obj[3]>0:
									# {"feature": "Direction_same", "instances": 18, "metric_value": 0.0926, "depth": 9}
									if obj[10]<=0:
										return 'True'
									elif obj[10]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[1]<=0:
											return 'True'
										elif obj[1]>0:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[7]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Bar", "instances": 9, "metric_value": 0.2963, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>18.149362003525606:
						# {"feature": "Time", "instances": 118, "metric_value": 0.2949, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Age", "instances": 71, "metric_value": 0.3361, "depth": 7}
							if obj[4]>0:
								# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.4015, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Education", "instances": 52, "metric_value": 0.4294, "depth": 9}
									if obj[5]>0:
										# {"feature": "Bar", "instances": 31, "metric_value": 0.4508, "depth": 10}
										if obj[7]<=1.0:
											# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4316, "depth": 11}
											if obj[10]>0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>1.0:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 0.3333, "depth": 11}
											if obj[10]>0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4333, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=0:
										# {"feature": "Bar", "instances": 21, "metric_value": 0.3464, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.2792, "depth": 11}
											if obj[10]>0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.175, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.4167, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[7]>2.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[10]>0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>2.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							# {"feature": "Bar", "instances": 47, "metric_value": 0.1789, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Direction_same", "instances": 40, "metric_value": 0.1152, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Age", "instances": 34, "metric_value": 0.0515, "depth": 9}
									if obj[4]>0:
										return 'True'
									elif obj[4]<=0:
										# {"feature": "Education", "instances": 8, "metric_value": 0.125, "depth": 10}
										if obj[5]<=2:
											return 'True'
										elif obj[5]>2:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]>0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[5]<=0:
										return 'True'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[4]<=2:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>2.0:
								# {"feature": "Gender", "instances": 7, "metric_value": 0.2857, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[4]>1:
										# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=1:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 902, "metric_value": 0.349, "depth": 5}
					if obj[7]<=3.0:
						# {"feature": "Education", "instances": 848, "metric_value": 0.3366, "depth": 6}
						if obj[5]<=3:
							# {"feature": "Time", "instances": 804, "metric_value": 0.3474, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Occupation", "instances": 489, "metric_value": 0.3124, "depth": 8}
								if obj[6]>2.5454774682183086:
									# {"feature": "Restaurant20to50", "instances": 406, "metric_value": 0.334, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Age", "instances": 370, "metric_value": 0.3205, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Gender", "instances": 358, "metric_value": 0.3294, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 189, "metric_value": 0.3628, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 169, "metric_value": 0.292, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										# {"feature": "Gender", "instances": 36, "metric_value": 0.4198, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 18, "metric_value": 0.4444, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]>4:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Age", "instances": 18, "metric_value": 0.3214, "depth": 11}
											if obj[4]>1:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.2604, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=2.5454774682183086:
									# {"feature": "Age", "instances": 83, "metric_value": 0.1624, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.1414, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 74, "metric_value": 0.149, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 50, "metric_value": 0.1472, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.1528, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									elif obj[4]>6:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Age", "instances": 315, "metric_value": 0.3837, "depth": 8}
								if obj[4]>0:
									# {"feature": "Restaurant20to50", "instances": 279, "metric_value": 0.3631, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Gender", "instances": 163, "metric_value": 0.3966, "depth": 10}
										if obj[3]>0:
											# {"feature": "Occupation", "instances": 84, "metric_value": 0.4385, "depth": 11}
											if obj[6]<=16:
												# {"feature": "Direction_same", "instances": 72, "metric_value": 0.4861, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>16:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.1528, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Occupation", "instances": 79, "metric_value": 0.3146, "depth": 11}
											if obj[6]<=12:
												# {"feature": "Direction_same", "instances": 68, "metric_value": 0.2907, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>12:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Gender", "instances": 116, "metric_value": 0.2862, "depth": 10}
										if obj[3]>0:
											# {"feature": "Occupation", "instances": 72, "metric_value": 0.2166, "depth": 11}
											if obj[6]<=9:
												# {"feature": "Direction_same", "instances": 47, "metric_value": 0.2535, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>9:
												# {"feature": "Direction_same", "instances": 25, "metric_value": 0.1472, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Occupation", "instances": 44, "metric_value": 0.3886, "depth": 11}
											if obj[6]<=9:
												# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3457, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>9:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4567, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Occupation", "instances": 36, "metric_value": 0.4375, "depth": 9}
									if obj[6]<=10:
										# {"feature": "Gender", "instances": 32, "metric_value": 0.4511, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.4306, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4717, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.381, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>10:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[5]>3:
							# {"feature": "Time", "instances": 44, "metric_value": 0.0744, "depth": 7}
							if obj[1]<=3:
								return 'True'
							elif obj[1]>3:
								# {"feature": "Age", "instances": 11, "metric_value": 0.1636, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Occupation", "instances": 10, "metric_value": 0.1333, "depth": 9}
									if obj[6]>1:
										return 'True'
									elif obj[6]<=1:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[9]>1.0:
												return 'False'
											elif obj[9]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[7]>3.0:
						# {"feature": "Time", "instances": 54, "metric_value": 0.4364, "depth": 6}
						if obj[1]>0:
							# {"feature": "Age", "instances": 44, "metric_value": 0.43, "depth": 7}
							if obj[4]>0:
								# {"feature": "Gender", "instances": 35, "metric_value": 0.4709, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Education", "instances": 27, "metric_value": 0.4937, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Occupation", "instances": 16, "metric_value": 0.4896, "depth": 10}
										if obj[6]<=14:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4857, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>14:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]>2:
										# {"feature": "Occupation", "instances": 11, "metric_value": 0.4959, "depth": 10}
										if obj[6]<=1:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4959, "depth": 11}
											if obj[9]<=4.0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.3333, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[9]>0.0:
											return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[6]<=7:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[6]<=7:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=4.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.0, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Age", "instances": 10, "metric_value": 0.1778, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.1481, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]<=0.0:
											return 'False'
										elif obj[9]>0.0:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]>4:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[11]>2:
				# {"feature": "Age", "instances": 271, "metric_value": 0.4863, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Passanger", "instances": 227, "metric_value": 0.4831, "depth": 5}
					if obj[0]>0:
						# {"feature": "Occupation", "instances": 220, "metric_value": 0.4853, "depth": 6}
						if obj[6]<=11.96483872460614:
							# {"feature": "Time", "instances": 185, "metric_value": 0.4917, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Restaurant20to50", "instances": 146, "metric_value": 0.4785, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Bar", "instances": 130, "metric_value": 0.4925, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Gender", "instances": 101, "metric_value": 0.4928, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 51, "metric_value": 0.4801, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 38, "metric_value": 0.4986, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.426, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 50, "metric_value": 0.4716, "depth": 11}
											if obj[5]>1:
												# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4518, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4989, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Education", "instances": 29, "metric_value": 0.4429, "depth": 10}
										if obj[5]>1:
											# {"feature": "Gender", "instances": 20, "metric_value": 0.3792, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]<=1:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.4333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>2.0:
									# {"feature": "Education", "instances": 16, "metric_value": 0.0, "depth": 9}
									if obj[5]>0:
										return 'False'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>1:
								# {"feature": "Gender", "instances": 39, "metric_value": 0.4282, "depth": 8}
								if obj[3]>0:
									# {"feature": "Education", "instances": 21, "metric_value": 0.4333, "depth": 9}
									if obj[5]>0:
										# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4167, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Bar", "instances": 10, "metric_value": 0.4167, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1.0:
												return 'False'
											elif obj[7]>1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[5]<=0:
										# {"feature": "Bar", "instances": 5, "metric_value": 0.2, "depth": 10}
										if obj[7]<=0.0:
											return 'True'
										elif obj[7]>0.0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[9]<=1.0:
												return 'True'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.2745, "depth": 9}
									if obj[9]>-1.0:
										# {"feature": "Education", "instances": 17, "metric_value": 0.2638, "depth": 10}
										if obj[5]>0:
											# {"feature": "Bar", "instances": 11, "metric_value": 0.1558, "depth": 11}
											if obj[7]>1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[6]>11.96483872460614:
							# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.3469, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Education", "instances": 21, "metric_value": 0.2143, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Time", "instances": 12, "metric_value": 0.2727, "depth": 9}
									if obj[1]>0:
										# {"feature": "Bar", "instances": 11, "metric_value": 0.2727, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[5]>2:
									return 'True'
								else: return 'True'
							elif obj[9]>1.0:
								# {"feature": "Gender", "instances": 14, "metric_value": 0.4082, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Education", "instances": 7, "metric_value": 0.1905, "depth": 9}
									if obj[5]<=2:
										return 'False'
									elif obj[5]>2:
										# {"feature": "Time", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[1]<=1:
											return 'True'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 7, "metric_value": 0.3429, "depth": 9}
									if obj[5]>0:
										# {"feature": "Time", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[1]>0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[7]<=2.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>5:
					# {"feature": "Education", "instances": 44, "metric_value": 0.3598, "depth": 5}
					if obj[5]>0:
						# {"feature": "Occupation", "instances": 31, "metric_value": 0.2688, "depth": 6}
						if obj[6]<=16:
							# {"feature": "Bar", "instances": 30, "metric_value": 0.2299, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.2146, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Gender", "instances": 18, "metric_value": 0.3306, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.3111, "depth": 10}
										if obj[1]>0:
											# {"feature": "Passanger", "instances": 9, "metric_value": 0.3457, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Time", "instances": 8, "metric_value": 0.2, "depth": 10}
										if obj[1]>0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[7]>2.0:
								return 'True'
							else: return 'True'
						elif obj[6]>16:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						# {"feature": "Time", "instances": 13, "metric_value": 0.2462, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.1333, "depth": 7}
							if obj[7]<=0.0:
								return 'True'
							elif obj[7]>0.0:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[6]>6:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[9]<=1.0:
										return 'True'
									elif obj[9]>1.0:
										return 'False'
									else: return 'False'
								elif obj[6]<=6:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2260, "metric_value": 0.4558, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Occupation", "instances": 1577, "metric_value": 0.4395, "depth": 3}
			if obj[6]>1.8509661496426837:
				# {"feature": "Education", "instances": 1312, "metric_value": 0.4571, "depth": 4}
				if obj[5]>0:
					# {"feature": "Coffeehouse", "instances": 846, "metric_value": 0.4314, "depth": 5}
					if obj[8]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 795, "metric_value": 0.441, "depth": 6}
						if obj[9]<=1.0:
							# {"feature": "Passanger", "instances": 570, "metric_value": 0.4164, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Time", "instances": 490, "metric_value": 0.3949, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Distance", "instances": 330, "metric_value": 0.4363, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Age", "instances": 242, "metric_value": 0.4578, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Direction_same", "instances": 230, "metric_value": 0.4562, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 151, "metric_value": 0.4577, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 79, "metric_value": 0.4477, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4792, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>2:
										# {"feature": "Gender", "instances": 88, "metric_value": 0.3489, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 45, "metric_value": 0.2538, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Direction_same", "instances": 38, "metric_value": 0.3006, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]>4:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Age", "instances": 43, "metric_value": 0.4175, "depth": 11}
											if obj[4]<=6:
												# {"feature": "Direction_same", "instances": 42, "metric_value": 0.4274, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]>6:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Gender", "instances": 160, "metric_value": 0.2896, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 87, "metric_value": 0.2112, "depth": 10}
										if obj[4]>0:
											# {"feature": "Direction_same", "instances": 73, "metric_value": 0.1689, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 64, "metric_value": 0.1357, "depth": 12}
												if obj[11]<=1:
													return 'False'
												elif obj[11]>1:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=0:
											# {"feature": "Distance", "instances": 14, "metric_value": 0.3956, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.426, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Age", "instances": 73, "metric_value": 0.3558, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Distance", "instances": 72, "metric_value": 0.3525, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 68, "metric_value": 0.3433, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Time", "instances": 80, "metric_value": 0.4795, "depth": 8}
								if obj[1]>0:
									# {"feature": "Age", "instances": 78, "metric_value": 0.4854, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Gender", "instances": 44, "metric_value": 0.4709, "depth": 10}
										if obj[3]>0:
											# {"feature": "Distance", "instances": 23, "metric_value": 0.4415, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4753, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 21, "metric_value": 0.4412, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4567, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>2:
										# {"feature": "Gender", "instances": 34, "metric_value": 0.4917, "depth": 10}
										if obj[3]>0:
											# {"feature": "Distance", "instances": 24, "metric_value": 0.4841, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 10, "metric_value": 0.3, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[9]>1.0:
							# {"feature": "Age", "instances": 225, "metric_value": 0.4756, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Gender", "instances": 113, "metric_value": 0.4419, "depth": 8}
								if obj[3]>0:
									# {"feature": "Direction_same", "instances": 58, "metric_value": 0.3752, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Passanger", "instances": 50, "metric_value": 0.414, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Distance", "instances": 33, "metric_value": 0.4026, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Time", "instances": 20, "metric_value": 0.4768, "depth": 12}
												if obj[1]>2:
													return 'True'
												elif obj[1]<=2:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Time", "instances": 13, "metric_value": 0.2462, "depth": 12}
												if obj[1]>0:
													return 'False'
												elif obj[1]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Time", "instances": 17, "metric_value": 0.2206, "depth": 11}
											if obj[1]>2:
												return 'False'
											elif obj[1]<=2:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.4286, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Time", "instances": 55, "metric_value": 0.4705, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Passanger", "instances": 30, "metric_value": 0.4828, "depth": 10}
										if obj[0]>0:
											# {"feature": "Distance", "instances": 29, "metric_value": 0.4946, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.4917, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>2:
										# {"feature": "Direction_same", "instances": 25, "metric_value": 0.3967, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Passanger", "instances": 24, "metric_value": 0.3698, "depth": 11}
											if obj[0]>0:
												# {"feature": "Distance", "instances": 16, "metric_value": 0.2727, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[0]<=0:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.4667, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[4]>2:
								# {"feature": "Time", "instances": 112, "metric_value": 0.4817, "depth": 8}
								if obj[1]>0:
									# {"feature": "Passanger", "instances": 77, "metric_value": 0.4521, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Gender", "instances": 59, "metric_value": 0.452, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 45, "metric_value": 0.4751, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 37, "metric_value": 0.4963, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3214, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 12, "metric_value": 0.35, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Distance", "instances": 18, "metric_value": 0.3819, "depth": 10}
										if obj[11]>1:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.4062, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Passanger", "instances": 35, "metric_value": 0.402, "depth": 9}
									if obj[0]>0:
										# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4307, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Distance", "instances": 16, "metric_value": 0.4667, "depth": 11}
											if obj[11]>1:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.4889, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										elif obj[10]>0:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.3231, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[11]<=1:
													return 'True'
												elif obj[11]>1:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>3.0:
						# {"feature": "Distance", "instances": 51, "metric_value": 0.1696, "depth": 6}
						if obj[11]<=2:
							# {"feature": "Time", "instances": 37, "metric_value": 0.2194, "depth": 7}
							if obj[1]>2:
								# {"feature": "Gender", "instances": 19, "metric_value": 0.0789, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									# {"feature": "Age", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[4]<=1:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=2:
								# {"feature": "Age", "instances": 18, "metric_value": 0.3175, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.381, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Passanger", "instances": 12, "metric_value": 0.4333, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Gender", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]>2:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[4]>4:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[11]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Age", "instances": 466, "metric_value": 0.4869, "depth": 5}
					if obj[4]>2:
						# {"feature": "Coffeehouse", "instances": 296, "metric_value": 0.488, "depth": 6}
						if obj[8]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 260, "metric_value": 0.4892, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Distance", "instances": 248, "metric_value": 0.4956, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Time", "instances": 202, "metric_value": 0.493, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Passanger", "instances": 148, "metric_value": 0.4945, "depth": 10}
										if obj[0]>0:
											# {"feature": "Direction_same", "instances": 134, "metric_value": 0.4976, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 87, "metric_value": 0.4992, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 47, "metric_value": 0.4943, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]<=0:
											# {"feature": "Gender", "instances": 14, "metric_value": 0.4317, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>3:
										# {"feature": "Passanger", "instances": 54, "metric_value": 0.4802, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Gender", "instances": 39, "metric_value": 0.4729, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4654, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>2:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4963, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[11]>2:
									# {"feature": "Gender", "instances": 46, "metric_value": 0.4638, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Time", "instances": 30, "metric_value": 0.416, "depth": 10}
										if obj[1]>0:
											# {"feature": "Passanger", "instances": 25, "metric_value": 0.4024, "depth": 11}
											if obj[0]>0:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3967, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[0]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Passanger", "instances": 16, "metric_value": 0.4667, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 15, "metric_value": 0.4974, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[9]>2.0:
								# {"feature": "Passanger", "instances": 12, "metric_value": 0.2381, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.2857, "depth": 9}
									if obj[11]>1:
										# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[10]<=0:
												return 'True'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>3.0:
							# {"feature": "Distance", "instances": 36, "metric_value": 0.3815, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Passanger", "instances": 30, "metric_value": 0.3359, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 26, "metric_value": 0.2896, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.1765, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 8, "metric_value": 0.3, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[1]>3:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>0:
										# {"feature": "Time", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3571, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												return 'True'
											else: return 'True'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]<=0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[11]>2:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.4, "depth": 8}
								if obj[0]>0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[9]<=1.0:
											return 'False'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=2:
						# {"feature": "Passanger", "instances": 170, "metric_value": 0.4518, "depth": 6}
						if obj[0]>0:
							# {"feature": "Time", "instances": 137, "metric_value": 0.4186, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Direction_same", "instances": 119, "metric_value": 0.4507, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Coffeehouse", "instances": 94, "metric_value": 0.4556, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.4853, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 46, "metric_value": 0.4497, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 38, "metric_value": 0.4579, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=2:
													return 'True'
												elif obj[11]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Distance", "instances": 21, "metric_value": 0.4542, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.3916, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]>2:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										# {"feature": "Gender", "instances": 27, "metric_value": 0.3065, "depth": 10}
										if obj[3]>0:
											# {"feature": "Distance", "instances": 14, "metric_value": 0.4069, "depth": 11}
											if obj[11]>1:
												# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.3967, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.1231, "depth": 11}
											if obj[9]<=1.0:
												return 'False'
											elif obj[9]>1.0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]>0:
									# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.3, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Gender", "instances": 20, "metric_value": 0.2357, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3214, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Distance", "instances": 12, "metric_value": 0.35, "depth": 12}
												if obj[11]<=1:
													return 'False'
												elif obj[11]>1:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[9]>1.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=1:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[9]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>3:
								# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.0556, "depth": 8}
								if obj[8]>-1.0:
									return 'False'
								elif obj[8]<=-1.0:
									# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.4692, "depth": 7}
							if obj[8]>-1.0:
								# {"feature": "Gender", "instances": 31, "metric_value": 0.4409, "depth": 8}
								if obj[3]>0:
									# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4267, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Distance", "instances": 15, "metric_value": 0.3744, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Time", "instances": 13, "metric_value": 0.3487, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>2:
											# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.419, "depth": 10}
										if obj[1]>0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.381, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>1:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.0, "depth": 9}
									if obj[9]<=1.0:
										return 'False'
									elif obj[9]>1.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]<=-1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[6]<=1.8509661496426837:
				# {"feature": "Gender", "instances": 265, "metric_value": 0.312, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 201, "metric_value": 0.2578, "depth": 5}
					if obj[5]<=4:
						# {"feature": "Restaurant20to50", "instances": 196, "metric_value": 0.2442, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Distance", "instances": 166, "metric_value": 0.2823, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Time", "instances": 134, "metric_value": 0.3136, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Direction_same", "instances": 68, "metric_value": 0.3737, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Age", "instances": 34, "metric_value": 0.4183, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.3077, "depth": 11}
											if obj[8]<=2.0:
												# {"feature": "Passanger", "instances": 13, "metric_value": 0.4231, "depth": 12}
												if obj[0]<=2:
													return 'False'
												elif obj[0]>2:
													return 'False'
												else: return 'False'
											elif obj[8]>2.0:
												return 'False'
											else: return 'False'
										elif obj[4]>3:
											# {"feature": "Passanger", "instances": 16, "metric_value": 0.4286, "depth": 11}
											if obj[0]<=2:
												# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.4396, "depth": 12}
												if obj[8]<=2.0:
													return 'False'
												elif obj[8]>2.0:
													return 'True'
												else: return 'True'
											elif obj[0]>2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>0:
										# {"feature": "Age", "instances": 34, "metric_value": 0.2458, "depth": 10}
										if obj[4]>0:
											# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.1817, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Passanger", "instances": 18, "metric_value": 0.1049, "depth": 12}
												if obj[0]<=1:
													return 'False'
												else: return 'False'
											elif obj[8]>1.0:
												# {"feature": "Passanger", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[0]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=0:
											# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[8]>1.0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[0]<=1:
													return 'False'
												elif obj[0]>1:
													return 'False'
												else: return 'False'
											elif obj[8]<=1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Passanger", "instances": 66, "metric_value": 0.2278, "depth": 9}
									if obj[0]>0:
										# {"feature": "Age", "instances": 60, "metric_value": 0.196, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Coffeehouse", "instances": 58, "metric_value": 0.1814, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Direction_same", "instances": 32, "metric_value": 0.102, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[8]>1.0:
												# {"feature": "Direction_same", "instances": 26, "metric_value": 0.2585, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]<=0:
										# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[4]>4:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]<=4:
												return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[11]>2:
								# {"feature": "Passanger", "instances": 32, "metric_value": 0.0605, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.0565, "depth": 9}
									if obj[8]>0.0:
										return 'False'
									elif obj[8]<=0.0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[4]<=4:
											return 'False'
										elif obj[4]>4:
											# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[5]>4:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.2667, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 7}
							if obj[1]>0:
								# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[4]<=7:
									# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=0.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Coffeehouse", "instances": 64, "metric_value": 0.3705, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Restaurant20to50", "instances": 56, "metric_value": 0.3444, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Passanger", "instances": 42, "metric_value": 0.4408, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Education", "instances": 35, "metric_value": 0.4114, "depth": 8}
								if obj[5]>0:
									# {"feature": "Age", "instances": 20, "metric_value": 0.4, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Time", "instances": 16, "metric_value": 0.4583, "depth": 10}
										if obj[1]>0:
											# {"feature": "Distance", "instances": 12, "metric_value": 0.4242, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4621, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>4:
										return 'False'
									else: return 'False'
								elif obj[5]<=0:
									# {"feature": "Age", "instances": 15, "metric_value": 0.25, "depth": 9}
									if obj[4]>2:
										# {"feature": "Time", "instances": 8, "metric_value": 0.4286, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4286, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Time", "instances": 7, "metric_value": 0.381, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Education", "instances": 6, "metric_value": 0.2667, "depth": 9}
									if obj[5]<=1:
										# {"feature": "Age", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>0:
											return 'True'
										else: return 'True'
									elif obj[5]>1:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[8]>2.0:
						# {"feature": "Age", "instances": 8, "metric_value": 0.1667, "depth": 6}
						if obj[4]>4:
							return 'True'
						elif obj[4]<=4:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[7]>1.0:
			# {"feature": "Restaurant20to50", "instances": 683, "metric_value": 0.4668, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Passanger", "instances": 562, "metric_value": 0.4802, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 474, "metric_value": 0.486, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 308, "metric_value": 0.4768, "depth": 6}
						if obj[6]>0:
							# {"feature": "Direction_same", "instances": 304, "metric_value": 0.4789, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Age", "instances": 215, "metric_value": 0.4818, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Distance", "instances": 122, "metric_value": 0.4885, "depth": 9}
									if obj[11]>1:
										# {"feature": "Education", "instances": 116, "metric_value": 0.4922, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Coffeehouse", "instances": 111, "metric_value": 0.4963, "depth": 11}
											if obj[8]<=2.0:
												# {"feature": "Gender", "instances": 79, "metric_value": 0.497, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[8]>2.0:
												# {"feature": "Gender", "instances": 32, "metric_value": 0.4861, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[5]>3:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[8]<=0.0:
													return 'True'
												elif obj[8]>0.0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]<=1:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[3]<=0:
											return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]>3:
									# {"feature": "Coffeehouse", "instances": 93, "metric_value": 0.4509, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Distance", "instances": 79, "metric_value": 0.4511, "depth": 10}
										if obj[11]>1:
											# {"feature": "Education", "instances": 77, "metric_value": 0.4554, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Gender", "instances": 74, "metric_value": 0.4517, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>3:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>3.0:
										# {"feature": "Gender", "instances": 14, "metric_value": 0.2857, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.4286, "depth": 11}
											if obj[5]>0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[11]<=2:
													return 'True'
												elif obj[11]>2:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[11]<=2:
													return 'True'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[10]>0:
								# {"feature": "Coffeehouse", "instances": 89, "metric_value": 0.4305, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Education", "instances": 81, "metric_value": 0.4194, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Age", "instances": 78, "metric_value": 0.4302, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Distance", "instances": 76, "metric_value": 0.4411, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Gender", "instances": 65, "metric_value": 0.4341, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[11]>1:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.4182, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									elif obj[5]>3:
										return 'True'
									else: return 'True'
								elif obj[8]>3.0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.3, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[4]>1:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[4]<=1:
												return 'True'
											elif obj[4]>1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[5]>2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						# {"feature": "Occupation", "instances": 166, "metric_value": 0.4852, "depth": 6}
						if obj[6]<=8.74698795180723:
							# {"feature": "Coffeehouse", "instances": 97, "metric_value": 0.4678, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Age", "instances": 61, "metric_value": 0.4514, "depth": 8}
								if obj[4]>1:
									# {"feature": "Education", "instances": 43, "metric_value": 0.4411, "depth": 9}
									if obj[5]>1:
										# {"feature": "Direction_same", "instances": 25, "metric_value": 0.3967, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Distance", "instances": 24, "metric_value": 0.4058, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.4234, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									elif obj[5]<=1:
										# {"feature": "Distance", "instances": 18, "metric_value": 0.4618, "depth": 10}
										if obj[11]<=1:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.4606, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>1:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=1:
									# {"feature": "Education", "instances": 18, "metric_value": 0.3333, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.3667, "depth": 10}
										if obj[11]>1:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4333, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[11]<=1:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]<=1.0:
								# {"feature": "Education", "instances": 36, "metric_value": 0.3838, "depth": 8}
								if obj[5]>0:
									# {"feature": "Age", "instances": 25, "metric_value": 0.4528, "depth": 9}
									if obj[4]<=1:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.3594, "depth": 10}
										if obj[11]>1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]<=1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.2, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>1:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.3333, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]>1:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=0:
									# {"feature": "Age", "instances": 11, "metric_value": 0.1364, "depth": 9}
									if obj[4]>1:
										return 'False'
									elif obj[4]<=1:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[11]>1:
												return 'True'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>8.74698795180723:
							# {"feature": "Gender", "instances": 69, "metric_value": 0.473, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Direction_same", "instances": 51, "metric_value": 0.4802, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Age", "instances": 49, "metric_value": 0.488, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Distance", "instances": 31, "metric_value": 0.4578, "depth": 10}
										if obj[11]<=1:
											# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.4421, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Education", "instances": 19, "metric_value": 0.432, "depth": 12}
												if obj[5]<=2:
													return 'True'
												elif obj[5]>2:
													return 'False'
												else: return 'False'
											elif obj[8]>3.0:
												return 'True'
											else: return 'True'
										elif obj[11]>1:
											# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.404, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Education", "instances": 9, "metric_value": 0.4815, "depth": 12}
												if obj[5]>1:
													return 'True'
												elif obj[5]<=1:
													return 'False'
												else: return 'False'
											elif obj[8]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>2:
										# {"feature": "Education", "instances": 18, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.4167, "depth": 11}
											if obj[8]>1.0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											elif obj[8]<=1.0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=1:
													return 'False'
												elif obj[11]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>1:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.25, "depth": 11}
											if obj[11]>1:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[8]>1.0:
													return 'False'
												elif obj[8]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]>0:
									return 'False'
								else: return 'False'
							elif obj[3]>0:
								# {"feature": "Age", "instances": 18, "metric_value": 0.303, "depth": 8}
								if obj[4]>2:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.3636, "depth": 9}
									if obj[11]<=1:
										# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[8]>1.0:
											# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												return 'True'
											else: return 'True'
										elif obj[8]<=1.0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[11]>1:
										return 'False'
									else: return 'False'
								elif obj[4]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 88, "metric_value": 0.3215, "depth": 5}
					if obj[1]>2:
						# {"feature": "Age", "instances": 67, "metric_value": 0.2508, "depth": 6}
						if obj[4]<=4:
							# {"feature": "Occupation", "instances": 64, "metric_value": 0.2299, "depth": 7}
							if obj[6]<=14:
								# {"feature": "Gender", "instances": 50, "metric_value": 0.165, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.0581, "depth": 9}
									if obj[8]>0.0:
										return 'True'
									elif obj[8]<=0.0:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.1714, "depth": 10}
										if obj[11]>1:
											# {"feature": "Education", "instances": 7, "metric_value": 0.2286, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[11]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>0:
									# {"feature": "Distance", "instances": 19, "metric_value": 0.2877, "depth": 9}
									if obj[11]>1:
										# {"feature": "Education", "instances": 15, "metric_value": 0.1238, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.127, "depth": 11}
											if obj[8]>1.0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[8]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>2:
											return 'False'
										else: return 'False'
									elif obj[11]<=1:
										# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[5]>0:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[8]>0.0:
												return 'False'
											elif obj[8]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[6]>14:
								# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.3297, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.2564, "depth": 9}
									if obj[11]>1:
										# {"feature": "Education", "instances": 12, "metric_value": 0.2381, "depth": 10}
										if obj[5]>1:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.381, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[5]<=1:
											return 'True'
										else: return 'True'
									elif obj[11]<=1:
										return 'False'
									else: return 'False'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]>4:
							# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=2:
						# {"feature": "Occupation", "instances": 21, "metric_value": 0.3079, "depth": 6}
						if obj[6]<=12:
							# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.28, "depth": 7}
							if obj[8]>0.0:
								# {"feature": "Education", "instances": 10, "metric_value": 0.375, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Age", "instances": 8, "metric_value": 0.3571, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[5]>2:
									return 'False'
								else: return 'False'
							elif obj[8]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[6]>12:
							# {"feature": "Gender", "instances": 6, "metric_value": 0.0, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[9]>2.0:
				# {"feature": "Age", "instances": 121, "metric_value": 0.343, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Occupation", "instances": 108, "metric_value": 0.2892, "depth": 5}
					if obj[6]<=9:
						# {"feature": "Coffeehouse", "instances": 64, "metric_value": 0.1608, "depth": 6}
						if obj[8]<=3.0:
							# {"feature": "Distance", "instances": 43, "metric_value": 0.0851, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Passanger", "instances": 36, "metric_value": 0.05, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.1667, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.2667, "depth": 10}
										if obj[1]>2:
											# {"feature": "Education", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												return 'True'
											else: return 'True'
										elif obj[1]<=2:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[11]>2:
								# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>3.0:
							# {"feature": "Distance", "instances": 21, "metric_value": 0.2665, "depth": 7}
							if obj[11]>1:
								# {"feature": "Passanger", "instances": 13, "metric_value": 0.0769, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[5]<=4:
										return 'False'
									elif obj[5]>4:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[11]<=1:
								# {"feature": "Time", "instances": 8, "metric_value": 0.3, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=4:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[10]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>9:
						# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.4211, "depth": 6}
						if obj[8]<=3.0:
							# {"feature": "Passanger", "instances": 38, "metric_value": 0.463, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Time", "instances": 29, "metric_value": 0.4497, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Education", "instances": 19, "metric_value": 0.4173, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Gender", "instances": 12, "metric_value": 0.2857, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.4286, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[5]>2:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.4286, "depth": 10}
										if obj[11]>1:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[11]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3111, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Distance", "instances": 9, "metric_value": 0.1944, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Education", "instances": 8, "metric_value": 0.1875, "depth": 11}
											if obj[5]>1:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[5]<=1:
												return 'False'
											else: return 'False'
										elif obj[11]>2:
											return 'True'
										else: return 'True'
									elif obj[10]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.1481, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[1]>2:
										# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[5]<=1:
											return 'True'
										elif obj[5]>1:
											return 'False'
										else: return 'False'
									elif obj[1]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>3.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>4:
					# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3916, "depth": 5}
					if obj[10]<=0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.3697, "depth": 6}
						if obj[6]>5:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[6]<=5:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.0, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'False'
