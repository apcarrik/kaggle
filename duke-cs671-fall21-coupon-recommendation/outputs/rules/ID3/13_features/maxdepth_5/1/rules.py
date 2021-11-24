def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4722, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5903, "metric_value": 0.4569, "depth": 2}
		if obj[9]<=1.0:
			# {"feature": "Passanger", "instances": 3018, "metric_value": 0.4857, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 1928, "metric_value": 0.4872, "depth": 4}
				if obj[12]<=1:
					# {"feature": "Time", "instances": 1066, "metric_value": 0.4791, "depth": 5}
					if obj[1]>0:
						# {"feature": "Direction_same", "instances": 704, "metric_value": 0.457, "depth": 6}
						if obj[11]>0:
							# {"feature": "Occupation", "instances": 360, "metric_value": 0.4901, "depth": 7}
							if obj[7]<=20.37285734786367:
								# {"feature": "Bar", "instances": 337, "metric_value": 0.4933, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Age", "instances": 270, "metric_value": 0.4871, "depth": 9}
									if obj[4]>0:
										# {"feature": "Restaurant20to50", "instances": 226, "metric_value": 0.4909, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Education", "instances": 219, "metric_value": 0.4965, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Gender", "instances": 193, "metric_value": 0.4987, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 119, "metric_value": 0.4957, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 74, "metric_value": 0.4905, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[6]>3:
												# {"feature": "Children", "instances": 26, "metric_value": 0.4685, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 22, "metric_value": 0.4589, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>2.0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.1429, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=4:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Children", "instances": 44, "metric_value": 0.3971, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 25, "metric_value": 0.2824, "depth": 11}
											if obj[6]<=1:
												# {"feature": "Gender", "instances": 17, "metric_value": 0.4039, "depth": 12}
												if obj[3]>0:
													# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.3852, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													elif obj[10]>1.0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>1:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 19, "metric_value": 0.3789, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 15, "metric_value": 0.4286, "depth": 12}
												if obj[6]>0:
													# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.4317, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													elif obj[10]>0.0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									# {"feature": "Age", "instances": 67, "metric_value": 0.4228, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.4511, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Education", "instances": 56, "metric_value": 0.4497, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Gender", "instances": 54, "metric_value": 0.4542, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 38, "metric_value": 0.4807, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 16, "metric_value": 0.3571, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>2:
												return 'False'
											else: return 'False'
										elif obj[10]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.15, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]>20.37285734786367:
								# {"feature": "Age", "instances": 23, "metric_value": 0.2977, "depth": 8}
								if obj[4]>2:
									# {"feature": "Gender", "instances": 13, "metric_value": 0.1026, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=2:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.4167, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Children", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[6]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=3.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=0:
							# {"feature": "Children", "instances": 344, "metric_value": 0.4134, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Education", "instances": 229, "metric_value": 0.4327, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Bar", "instances": 193, "metric_value": 0.4158, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 134, "metric_value": 0.3885, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Occupation", "instances": 130, "metric_value": 0.3969, "depth": 11}
											if obj[7]>0:
												# {"feature": "Age", "instances": 127, "metric_value": 0.4039, "depth": 12}
												if obj[4]<=6:
													# {"feature": "Gender", "instances": 120, "metric_value": 0.4124, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[4]>6:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Restaurant20to50", "instances": 59, "metric_value": 0.4344, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Occupation", "instances": 46, "metric_value": 0.4008, "depth": 11}
											if obj[7]<=12:
												# {"feature": "Age", "instances": 41, "metric_value": 0.4388, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Gender", "instances": 22, "metric_value": 0.381, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[4]>1:
													# {"feature": "Gender", "instances": 19, "metric_value": 0.4737, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]>12:
												return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Occupation", "instances": 13, "metric_value": 0.2462, "depth": 11}
											if obj[7]>2:
												# {"feature": "Age", "instances": 10, "metric_value": 0.2857, "depth": 12}
												if obj[4]>0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]<=2:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Occupation", "instances": 36, "metric_value": 0.4362, "depth": 9}
									if obj[7]<=6:
										# {"feature": "Age", "instances": 27, "metric_value": 0.4444, "depth": 10}
										if obj[4]>0:
											# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4698, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Bar", "instances": 18, "metric_value": 0.4752, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Gender", "instances": 13, "metric_value": 0.4689, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2381, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Bar", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>6:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.2222, "depth": 10}
										if obj[10]<=1.0:
											return 'False'
										elif obj[10]>1.0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[5]>0:
								# {"feature": "Bar", "instances": 115, "metric_value": 0.3388, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Occupation", "instances": 109, "metric_value": 0.3184, "depth": 9}
									if obj[7]<=19:
										# {"feature": "Education", "instances": 104, "metric_value": 0.3037, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Age", "instances": 87, "metric_value": 0.3356, "depth": 11}
											if obj[4]<=6:
												# {"feature": "Restaurant20to50", "instances": 82, "metric_value": 0.3517, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Gender", "instances": 62, "metric_value": 0.3828, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Gender", "instances": 20, "metric_value": 0.25, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>6:
												return 'True'
											else: return 'True'
										elif obj[6]>2:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.0941, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Age", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=3.0:
														return 'True'
													else: return 'True'
												elif obj[4]>3:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>19:
										# {"feature": "Age", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]>2.0:
									# {"feature": "Occupation", "instances": 6, "metric_value": 0.2667, "depth": 9}
									if obj[7]<=17:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[4]<=2:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[7]>17:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 362, "metric_value": 0.4901, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Gender", "instances": 355, "metric_value": 0.491, "depth": 7}
							if obj[3]>0:
								# {"feature": "Education", "instances": 182, "metric_value": 0.4812, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Children", "instances": 161, "metric_value": 0.4784, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Age", "instances": 99, "metric_value": 0.4848, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Occupation", "instances": 87, "metric_value": 0.4915, "depth": 11}
											if obj[7]>3:
												# {"feature": "Bar", "instances": 58, "metric_value": 0.4767, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4663, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4908, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]<=3:
												# {"feature": "Bar", "instances": 29, "metric_value": 0.4191, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3667, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4505, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[4]>5:
											# {"feature": "Occupation", "instances": 12, "metric_value": 0.35, "depth": 11}
											if obj[7]<=6:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.2667, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Bar", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													elif obj[8]>0.0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[7]>6:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Direction_same", "instances": 62, "metric_value": 0.4232, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Occupation", "instances": 42, "metric_value": 0.3592, "depth": 11}
											if obj[7]<=16:
												# {"feature": "Age", "instances": 35, "metric_value": 0.3943, "depth": 12}
												if obj[4]>1:
													# {"feature": "Bar", "instances": 25, "metric_value": 0.4528, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													elif obj[8]>0.0:
														return 'True'
													else: return 'True'
												elif obj[4]<=1:
													# {"feature": "Bar", "instances": 10, "metric_value": 0.1714, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													elif obj[8]>0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]>16:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Occupation", "instances": 20, "metric_value": 0.4118, "depth": 11}
											if obj[7]<=12:
												# {"feature": "Age", "instances": 17, "metric_value": 0.4135, "depth": 12}
												if obj[4]>1:
													# {"feature": "Bar", "instances": 11, "metric_value": 0.3961, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													elif obj[8]>0.0:
														return 'False'
													else: return 'False'
												elif obj[4]<=1:
													# {"feature": "Bar", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[8]>0.0:
														return 'True'
													elif obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]>12:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[6]>3:
									# {"feature": "Age", "instances": 21, "metric_value": 0.375, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Occupation", "instances": 16, "metric_value": 0.4271, "depth": 10}
										if obj[7]>1:
											# {"feature": "Bar", "instances": 12, "metric_value": 0.3333, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[8]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[7]<=1:
											# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[11]>0:
													# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[8]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>4:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Education", "instances": 173, "metric_value": 0.4646, "depth": 8}
								if obj[6]>1:
									# {"feature": "Bar", "instances": 99, "metric_value": 0.4817, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Occupation", "instances": 92, "metric_value": 0.4849, "depth": 10}
										if obj[7]>4:
											# {"feature": "Age", "instances": 78, "metric_value": 0.4875, "depth": 11}
											if obj[4]>0:
												# {"feature": "Direction_same", "instances": 60, "metric_value": 0.4852, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 36, "metric_value": 0.4722, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 24, "metric_value": 0.4958, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=0:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4691, "depth": 12}
												if obj[11]>0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.4921, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=4:
											# {"feature": "Age", "instances": 14, "metric_value": 0.3393, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Children", "instances": 8, "metric_value": 0.125, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[4]>4:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[8]>2.0:
										# {"feature": "Age", "instances": 7, "metric_value": 0.2143, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Occupation", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[7]>1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[7]<=1:
												return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=1:
									# {"feature": "Occupation", "instances": 74, "metric_value": 0.3902, "depth": 9}
									if obj[7]<=18:
										# {"feature": "Age", "instances": 64, "metric_value": 0.4418, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Bar", "instances": 50, "metric_value": 0.4653, "depth": 11}
											if obj[8]>-1.0:
												# {"feature": "Children", "instances": 49, "metric_value": 0.4709, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 36, "metric_value": 0.4603, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4872, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=-1.0:
												return 'True'
											else: return 'True'
										elif obj[4]>4:
											# {"feature": "Bar", "instances": 14, "metric_value": 0.2251, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1515, "depth": 12}
												if obj[11]>0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											elif obj[8]>1.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]>18:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[10]>2.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[12]>1:
					# {"feature": "Time", "instances": 862, "metric_value": 0.4813, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Direction_same", "instances": 705, "metric_value": 0.4721, "depth": 6}
						if obj[11]<=0:
							# {"feature": "Children", "instances": 528, "metric_value": 0.4596, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Bar", "instances": 335, "metric_value": 0.4715, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Age", "instances": 310, "metric_value": 0.4809, "depth": 9}
									if obj[4]>1:
										# {"feature": "Occupation", "instances": 175, "metric_value": 0.4665, "depth": 10}
										if obj[7]>0:
											# {"feature": "Education", "instances": 173, "metric_value": 0.4691, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 128, "metric_value": 0.4584, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Gender", "instances": 127, "metric_value": 0.4616, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[10]>2.0:
													return 'False'
												else: return 'False'
											elif obj[6]>2:
												# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.4866, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Gender", "instances": 32, "metric_value": 0.476, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													# {"feature": "Gender", "instances": 13, "metric_value": 0.4923, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[7]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]<=1:
										# {"feature": "Occupation", "instances": 135, "metric_value": 0.4886, "depth": 10}
										if obj[7]>4:
											# {"feature": "Restaurant20to50", "instances": 75, "metric_value": 0.4703, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Education", "instances": 74, "metric_value": 0.4684, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Gender", "instances": 63, "metric_value": 0.4618, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.4909, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												return 'True'
											else: return 'True'
										elif obj[7]<=4:
											# {"feature": "Restaurant20to50", "instances": 60, "metric_value": 0.4802, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Education", "instances": 42, "metric_value": 0.4868, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Gender", "instances": 38, "metric_value": 0.4931, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 18, "metric_value": 0.375, "depth": 12}
												if obj[3]>0:
													# {"feature": "Education", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[6]<=0:
														return 'False'
													elif obj[6]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Education", "instances": 8, "metric_value": 0.1875, "depth": 13}
													if obj[6]>2:
														return 'True'
													elif obj[6]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>2.0:
									# {"feature": "Education", "instances": 25, "metric_value": 0.2947, "depth": 9}
									if obj[6]>0:
										# {"feature": "Occupation", "instances": 19, "metric_value": 0.3618, "depth": 10}
										if obj[7]<=10:
											# {"feature": "Age", "instances": 16, "metric_value": 0.3718, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.3357, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.3737, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													elif obj[10]>1.0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[4]>1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>10:
											return 'False'
										else: return 'False'
									elif obj[6]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>0:
								# {"feature": "Gender", "instances": 193, "metric_value": 0.4126, "depth": 8}
								if obj[3]>0:
									# {"feature": "Occupation", "instances": 114, "metric_value": 0.3479, "depth": 9}
									if obj[7]>1:
										# {"feature": "Age", "instances": 95, "metric_value": 0.3113, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Bar", "instances": 69, "metric_value": 0.2646, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Education", "instances": 35, "metric_value": 0.3102, "depth": 12}
												if obj[6]>0:
													# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.2429, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													elif obj[10]>2.0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.329, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													elif obj[10]>1.0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]<=0.0:
												# {"feature": "Education", "instances": 34, "metric_value": 0.2029, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.1793, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													elif obj[10]>1.0:
														return 'False'
													else: return 'False'
												elif obj[6]>3:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[10]<=-1.0:
														return 'False'
													elif obj[10]>-1.0:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'False'
										elif obj[4]>3:
											# {"feature": "Bar", "instances": 26, "metric_value": 0.3798, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.2897, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Education", "instances": 9, "metric_value": 0.1944, "depth": 13}
													if obj[6]<=0:
														return 'False'
													elif obj[6]>0:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													# {"feature": "Education", "instances": 7, "metric_value": 0.381, "depth": 13}
													if obj[6]<=1:
														return 'False'
													elif obj[6]>1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]>0.0:
												# {"feature": "Education", "instances": 10, "metric_value": 0.4444, "depth": 12}
												if obj[6]>0:
													# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4167, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													elif obj[10]>1.0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=1:
										# {"feature": "Education", "instances": 19, "metric_value": 0.4164, "depth": 10}
										if obj[6]>0:
											# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Age", "instances": 9, "metric_value": 0.4, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Bar", "instances": 5, "metric_value": 0.2667, "depth": 13}
													if obj[8]>0.0:
														return 'True'
													elif obj[8]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[4]>3:
													# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													elif obj[8]>0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.0, "depth": 11}
											if obj[10]<=1.0:
												return 'False'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Age", "instances": 79, "metric_value": 0.4525, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Occupation", "instances": 72, "metric_value": 0.4806, "depth": 10}
										if obj[7]<=17:
											# {"feature": "Education", "instances": 63, "metric_value": 0.4916, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Bar", "instances": 62, "metric_value": 0.4907, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.4913, "depth": 13}
													if obj[10]>-1.0:
														return 'False'
													elif obj[10]<=-1.0:
														return 'False'
													else: return 'False'
												elif obj[8]>2.0:
													return 'True'
												else: return 'True'
											elif obj[6]>3:
												return 'True'
											else: return 'True'
										elif obj[7]>17:
											# {"feature": "Education", "instances": 9, "metric_value": 0.2222, "depth": 11}
											if obj[6]>1:
												return 'False'
											elif obj[6]<=1:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													elif obj[10]>2.0:
														return 'False'
													else: return 'False'
												elif obj[8]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>6:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[11]>0:
							# {"feature": "Education", "instances": 177, "metric_value": 0.4858, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Occupation", "instances": 144, "metric_value": 0.4859, "depth": 8}
								if obj[7]<=14.164944200311755:
									# {"feature": "Bar", "instances": 123, "metric_value": 0.4902, "depth": 9}
									if obj[8]>-1.0:
										# {"feature": "Restaurant20to50", "instances": 121, "metric_value": 0.4909, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Age", "instances": 119, "metric_value": 0.4941, "depth": 11}
											if obj[4]>0:
												# {"feature": "Children", "instances": 93, "metric_value": 0.4985, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 59, "metric_value": 0.4982, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 34, "metric_value": 0.4971, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]<=0:
												# {"feature": "Gender", "instances": 26, "metric_value": 0.3669, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 13, "metric_value": 0.2577, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 13, "metric_value": 0.4718, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>2.0:
											return 'True'
										else: return 'True'
									elif obj[8]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[7]>14.164944200311755:
									# {"feature": "Bar", "instances": 21, "metric_value": 0.3429, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.3636, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Age", "instances": 11, "metric_value": 0.3636, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>4:
												return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>2:
								# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.3663, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Occupation", "instances": 26, "metric_value": 0.3067, "depth": 9}
									if obj[7]>3:
										# {"feature": "Children", "instances": 17, "metric_value": 0.1412, "depth": 10}
										if obj[5]<=0:
											return 'False'
										elif obj[5]>0:
											# {"feature": "Age", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[4]>0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.0, "depth": 13}
													if obj[8]>0.0:
														return 'False'
													elif obj[8]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=3:
										# {"feature": "Children", "instances": 9, "metric_value": 0.4333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Age", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[4]>4:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[8]>0.0:
													return 'True'
												else: return 'True'
											elif obj[4]<=4:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[4]>1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]>1.0:
									# {"feature": "Age", "instances": 7, "metric_value": 0.2381, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[7]>12:
												return 'True'
											elif obj[7]<=12:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Age", "instances": 157, "metric_value": 0.4687, "depth": 6}
						if obj[4]<=4:
							# {"feature": "Occupation", "instances": 126, "metric_value": 0.4834, "depth": 7}
							if obj[7]<=8.73015873015873:
								# {"feature": "Bar", "instances": 67, "metric_value": 0.4636, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Education", "instances": 66, "metric_value": 0.4657, "depth": 9}
									if obj[6]<=1:
										# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.419, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Children", "instances": 35, "metric_value": 0.4305, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 20, "metric_value": 0.4101, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.4267, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[6]>1:
										# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.4494, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4937, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 20, "metric_value": 0.4933, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.4857, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>3.0:
									return 'False'
								else: return 'False'
							elif obj[7]>8.73015873015873:
								# {"feature": "Bar", "instances": 59, "metric_value": 0.4588, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Gender", "instances": 42, "metric_value": 0.458, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.3556, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Children", "instances": 15, "metric_value": 0.4405, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Education", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Education", "instances": 21, "metric_value": 0.4074, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.4375, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 16, "metric_value": 0.4909, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										elif obj[6]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									# {"feature": "Children", "instances": 17, "metric_value": 0.3137, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.3704, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.4889, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>4:
							# {"feature": "Occupation", "instances": 31, "metric_value": 0.28, "depth": 7}
							if obj[7]>4:
								# {"feature": "Bar", "instances": 24, "metric_value": 0.1667, "depth": 8}
								if obj[8]<=0.0:
									return 'True'
								elif obj[8]>0.0:
									# {"feature": "Education", "instances": 9, "metric_value": 0.3333, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									elif obj[6]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=4:
								# {"feature": "Education", "instances": 7, "metric_value": 0.2286, "depth": 8}
								if obj[6]>0:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 9}
									if obj[3]<=0:
										return 'False'
									elif obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[10]>1.0:
											return 'False'
										elif obj[10]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 1090, "metric_value": 0.458, "depth": 4}
				if obj[7]>1.7265574939131305:
					# {"feature": "Distance", "instances": 900, "metric_value": 0.469, "depth": 5}
					if obj[12]>1:
						# {"feature": "Time", "instances": 600, "metric_value": 0.4548, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 477, "metric_value": 0.4657, "depth": 7}
							if obj[6]>1:
								# {"feature": "Age", "instances": 249, "metric_value": 0.4794, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Bar", "instances": 144, "metric_value": 0.4592, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 93, "metric_value": 0.4782, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 71, "metric_value": 0.4908, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 37, "metric_value": 0.4908, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 34, "metric_value": 0.4797, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4654, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Gender", "instances": 22, "metric_value": 0.4227, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 12, "metric_value": 0.35, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.4762, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>0.0:
										# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.3908, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 44, "metric_value": 0.3727, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 23, "metric_value": 0.2551, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.1244, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 21, "metric_value": 0.3516, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.2604, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>2:
									# {"feature": "Bar", "instances": 105, "metric_value": 0.4819, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Gender", "instances": 68, "metric_value": 0.4905, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.4656, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Children", "instances": 38, "metric_value": 0.4654, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4321, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4986, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>2.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.47, "depth": 11}
											if obj[10]>1.0:
												# {"feature": "Children", "instances": 15, "metric_value": 0.4571, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=1.0:
												# {"feature": "Children", "instances": 14, "metric_value": 0.3937, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										# {"feature": "Gender", "instances": 37, "metric_value": 0.4401, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.4778, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 15, "metric_value": 0.497, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												# {"feature": "Children", "instances": 9, "metric_value": 0.4333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.348, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.3714, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]<=1:
								# {"feature": "Bar", "instances": 228, "metric_value": 0.4389, "depth": 8}
								if obj[8]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 114, "metric_value": 0.4611, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Age", "instances": 77, "metric_value": 0.4798, "depth": 10}
										if obj[4]>0:
											# {"feature": "Gender", "instances": 68, "metric_value": 0.4821, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 44, "metric_value": 0.4679, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4297, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 24, "metric_value": 0.472, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4983, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]<=0.0:
										# {"feature": "Age", "instances": 37, "metric_value": 0.3475, "depth": 10}
										if obj[4]>0:
											# {"feature": "Children", "instances": 28, "metric_value": 0.4365, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 18, "metric_value": 0.3571, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>0.0:
									# {"feature": "Age", "instances": 114, "metric_value": 0.3972, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Restaurant20to50", "instances": 99, "metric_value": 0.4158, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 80, "metric_value": 0.3895, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 41, "metric_value": 0.4434, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4764, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4012, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 39, "metric_value": 0.3257, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3403, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3047, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Gender", "instances": 19, "metric_value": 0.4164, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.2212, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.1558, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Children", "instances": 123, "metric_value": 0.3665, "depth": 7}
							if obj[5]>0:
								# {"feature": "Age", "instances": 73, "metric_value": 0.4576, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Education", "instances": 44, "metric_value": 0.4619, "depth": 9}
									if obj[6]>0:
										# {"feature": "Bar", "instances": 26, "metric_value": 0.4385, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.4105, "depth": 11}
											if obj[10]>-1.0:
												# {"feature": "Gender", "instances": 19, "metric_value": 0.4316, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=-1.0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[10]>1.0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=0:
										# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.4444, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.3889, "depth": 11}
											if obj[3]>0:
												# {"feature": "Bar", "instances": 12, "metric_value": 0.4381, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]>2:
									# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.3751, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Education", "instances": 20, "metric_value": 0.4133, "depth": 10}
										if obj[6]<=1:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.3556, "depth": 11}
											if obj[3]>0:
												# {"feature": "Bar", "instances": 12, "metric_value": 0.4381, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>1:
											# {"feature": "Bar", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>1.0:
										# {"feature": "Bar", "instances": 9, "metric_value": 0.1111, "depth": 10}
										if obj[8]<=1.0:
											return 'True'
										elif obj[8]>1.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[5]<=0:
								# {"feature": "Education", "instances": 50, "metric_value": 0.2057, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.2395, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Age", "instances": 34, "metric_value": 0.2049, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Bar", "instances": 31, "metric_value": 0.2228, "depth": 11}
											if obj[8]<=2.0:
												# {"feature": "Gender", "instances": 26, "metric_value": 0.1952, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.1172, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>2.0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>4:
											return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[4]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[6]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[12]<=1:
						# {"feature": "Children", "instances": 300, "metric_value": 0.4848, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Time", "instances": 170, "metric_value": 0.4752, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Bar", "instances": 110, "metric_value": 0.4738, "depth": 8}
								if obj[8]>-1.0:
									# {"feature": "Education", "instances": 105, "metric_value": 0.47, "depth": 9}
									if obj[6]>1:
										# {"feature": "Age", "instances": 59, "metric_value": 0.4401, "depth": 10}
										if obj[4]>0:
											# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.4453, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 39, "metric_value": 0.4252, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4132, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.4921, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											return 'False'
										else: return 'False'
									elif obj[6]<=1:
										# {"feature": "Age", "instances": 46, "metric_value": 0.4306, "depth": 10}
										if obj[4]>2:
											# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.4605, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.4752, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=2:
											# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.2167, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.2074, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[8]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[1]>2:
								# {"feature": "Education", "instances": 60, "metric_value": 0.4198, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Age", "instances": 54, "metric_value": 0.3982, "depth": 9}
									if obj[4]<=5:
										# {"feature": "Gender", "instances": 49, "metric_value": 0.3764, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.3048, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Bar", "instances": 21, "metric_value": 0.2429, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>2.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Bar", "instances": 9, "metric_value": 0.4286, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>2.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Bar", "instances": 19, "metric_value": 0.4334, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.4392, "depth": 12}
												if obj[10]<=3.0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>3.0:
													return 'True'
												else: return 'True'
											elif obj[8]>3.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>5:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.0, "depth": 10}
										if obj[10]>0.0:
											return 'False'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[6]>2:
									# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[8]>0.0:
										return 'False'
									elif obj[8]<=0.0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[4]>1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[10]<=0.0:
												return 'False'
											elif obj[10]>0.0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 130, "metric_value": 0.4492, "depth": 7}
							if obj[6]<=3:
								# {"feature": "Bar", "instances": 118, "metric_value": 0.465, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Age", "instances": 113, "metric_value": 0.4681, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Restaurant20to50", "instances": 101, "metric_value": 0.4578, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Time", "instances": 70, "metric_value": 0.431, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Gender", "instances": 35, "metric_value": 0.3812, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3967, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Gender", "instances": 35, "metric_value": 0.4789, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4875, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Time", "instances": 31, "metric_value": 0.4793, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Gender", "instances": 24, "metric_value": 0.4667, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>3:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2857, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>6:
										# {"feature": "Time", "instances": 12, "metric_value": 0.4545, "depth": 10}
										if obj[1]>0:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4621, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>2.0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.2, "depth": 9}
									if obj[4]<=2:
										return 'False'
									elif obj[4]>2:
										# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[1]>2:
											return 'False'
										elif obj[1]<=2:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[6]>3:
								# {"feature": "Time", "instances": 12, "metric_value": 0.1429, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Age", "instances": 7, "metric_value": 0.2143, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[10]>-1.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=-1.0:
												return 'True'
											else: return 'True'
										elif obj[8]>0.0:
											return 'True'
										else: return 'True'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[7]<=1.7265574939131305:
					# {"feature": "Age", "instances": 190, "metric_value": 0.3859, "depth": 5}
					if obj[4]>1:
						# {"feature": "Bar", "instances": 110, "metric_value": 0.415, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Time", "instances": 91, "metric_value": 0.4502, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Education", "instances": 51, "metric_value": 0.4808, "depth": 8}
								if obj[6]>0:
									# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.4583, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Distance", "instances": 24, "metric_value": 0.4778, "depth": 10}
										if obj[12]<=1:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4933, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[12]>1:
											# {"feature": "Children", "instances": 9, "metric_value": 0.4167, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4583, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>1.0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0:
									# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4029, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Gender", "instances": 21, "metric_value": 0.4063, "depth": 10}
										if obj[3]>0:
											# {"feature": "Children", "instances": 15, "metric_value": 0.3692, "depth": 11}
											if obj[5]>0:
												# {"feature": "Distance", "instances": 13, "metric_value": 0.3916, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.4167, "depth": 11}
											if obj[12]>1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[10]>1.0:
										# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[12]>1:
												return 'True'
											elif obj[12]<=1:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Education", "instances": 40, "metric_value": 0.3486, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Gender", "instances": 36, "metric_value": 0.3305, "depth": 9}
									if obj[3]>0:
										# {"feature": "Distance", "instances": 25, "metric_value": 0.3947, "depth": 10}
										if obj[12]>1:
											# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3529, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Children", "instances": 16, "metric_value": 0.3718, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[12]<=1:
											# {"feature": "Children", "instances": 8, "metric_value": 0.3571, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.3714, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Children", "instances": 11, "metric_value": 0.1558, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.2286, "depth": 11}
											if obj[12]>1:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3:
									# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>1.0:
							# {"feature": "Time", "instances": 19, "metric_value": 0.1849, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Distance", "instances": 13, "metric_value": 0.1026, "depth": 8}
								if obj[12]>1:
									return 'True'
								elif obj[12]<=1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[3]>0:
										# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[6]<=4:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>3:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[12]>1:
										# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[12]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]<=1:
						# {"feature": "Education", "instances": 80, "metric_value": 0.3123, "depth": 6}
						if obj[6]<=3:
							# {"feature": "Distance", "instances": 73, "metric_value": 0.3391, "depth": 7}
							if obj[12]>1:
								# {"feature": "Bar", "instances": 43, "metric_value": 0.2826, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Gender", "instances": 39, "metric_value": 0.2544, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.293, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Time", "instances": 21, "metric_value": 0.3492, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Children", "instances": 12, "metric_value": 0.2667, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Children", "instances": 9, "metric_value": 0.4286, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Time", "instances": 13, "metric_value": 0.1231, "depth": 10}
										if obj[1]>2:
											return 'True'
										elif obj[1]<=2:
											# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[1]<=3:
										return 'True'
									elif obj[1]>3:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[12]<=1:
								# {"feature": "Bar", "instances": 30, "metric_value": 0.3367, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.2278, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Time", "instances": 18, "metric_value": 0.188, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.2601, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>2:
											return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[1]<=0:
											return 'False'
										elif obj[1]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=0.0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.4444, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Children", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]>3:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[9]>1.0:
			# {"feature": "Distance", "instances": 2885, "metric_value": 0.412, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Passanger", "instances": 2614, "metric_value": 0.4001, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1699, "metric_value": 0.4228, "depth": 5}
					if obj[7]<=18.185882392956827:
						# {"feature": "Direction_same", "instances": 1580, "metric_value": 0.4321, "depth": 6}
						if obj[11]<=0:
							# {"feature": "Time", "instances": 1024, "metric_value": 0.4381, "depth": 7}
							if obj[1]>1:
								# {"feature": "Age", "instances": 553, "metric_value": 0.3955, "depth": 8}
								if obj[4]>0:
									# {"feature": "Bar", "instances": 472, "metric_value": 0.3798, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Gender", "instances": 289, "metric_value": 0.3396, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 171, "metric_value": 0.4008, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Education", "instances": 153, "metric_value": 0.4132, "depth": 12}
												if obj[6]>1:
													# {"feature": "Children", "instances": 94, "metric_value": 0.4251, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=1:
													# {"feature": "Children", "instances": 59, "metric_value": 0.3396, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												# {"feature": "Education", "instances": 18, "metric_value": 0.2708, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Children", "instances": 16, "metric_value": 0.3016, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 118, "metric_value": 0.2441, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 92, "metric_value": 0.2644, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Children", "instances": 84, "metric_value": 0.2449, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Children", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.1377, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Children", "instances": 19, "metric_value": 0.1842, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Education", "instances": 183, "metric_value": 0.4199, "depth": 10}
										if obj[6]>1:
											# {"feature": "Children", "instances": 136, "metric_value": 0.3892, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 93, "metric_value": 0.4205, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Gender", "instances": 84, "metric_value": 0.4439, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.1852, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 43, "metric_value": 0.2817, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.3804, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													elif obj[10]>2.0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.1029, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													elif obj[10]>1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=1:
											# {"feature": "Gender", "instances": 47, "metric_value": 0.466, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 27, "metric_value": 0.4079, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4503, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.1667, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													elif obj[10]>1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.4917, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Children", "instances": 12, "metric_value": 0.4792, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													# {"feature": "Children", "instances": 8, "metric_value": 0.4667, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Education", "instances": 81, "metric_value": 0.4418, "depth": 9}
									if obj[6]<=3:
										# {"feature": "Bar", "instances": 70, "metric_value": 0.4695, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.4407, "depth": 11}
											if obj[10]<=3.0:
												# {"feature": "Gender", "instances": 45, "metric_value": 0.4567, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 26, "metric_value": 0.4028, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 19, "metric_value": 0.4226, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[10]>3.0:
												return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.3326, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 13, "metric_value": 0.3462, "depth": 12}
												if obj[5]>0:
													# {"feature": "Gender", "instances": 12, "metric_value": 0.3704, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Children", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[5]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>3:
										# {"feature": "Gender", "instances": 11, "metric_value": 0.1364, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=1:
								# {"feature": "Bar", "instances": 471, "metric_value": 0.4804, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Children", "instances": 331, "metric_value": 0.4883, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Education", "instances": 206, "metric_value": 0.4772, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Age", "instances": 190, "metric_value": 0.4815, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Restaurant20to50", "instances": 158, "metric_value": 0.4871, "depth": 12}
												if obj[10]>-1.0:
													# {"feature": "Gender", "instances": 156, "metric_value": 0.492, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=-1.0:
													return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.4167, "depth": 12}
												if obj[10]<=3.0:
													# {"feature": "Gender", "instances": 30, "metric_value": 0.4352, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>3.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>3:
											# {"feature": "Age", "instances": 16, "metric_value": 0.3462, "depth": 11}
											if obj[4]<=3:
												# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.4249, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=1.0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Restaurant20to50", "instances": 125, "metric_value": 0.4885, "depth": 10}
										if obj[10]<=3.0:
											# {"feature": "Education", "instances": 119, "metric_value": 0.4912, "depth": 11}
											if obj[6]>1:
												# {"feature": "Gender", "instances": 87, "metric_value": 0.4847, "depth": 12}
												if obj[3]>0:
													# {"feature": "Age", "instances": 45, "metric_value": 0.4571, "depth": 13}
													if obj[4]>1:
														return 'True'
													elif obj[4]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Age", "instances": 42, "metric_value": 0.4615, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=1:
												# {"feature": "Age", "instances": 32, "metric_value": 0.4432, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Gender", "instances": 23, "metric_value": 0.4174, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]>3:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.4921, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[10]>3.0:
											# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[4]>0:
												return 'True'
											elif obj[4]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[6]<=4:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=0.0:
									# {"feature": "Age", "instances": 140, "metric_value": 0.4392, "depth": 9}
									if obj[4]>2:
										# {"feature": "Gender", "instances": 81, "metric_value": 0.4694, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 52, "metric_value": 0.4414, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Children", "instances": 42, "metric_value": 0.4125, "depth": 12}
												if obj[5]>0:
													# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.3687, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4935, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Children", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[5]>0:
													# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.4667, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Children", "instances": 29, "metric_value": 0.4642, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 19, "metric_value": 0.4211, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4182, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[6]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.3048, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 13}
													if obj[6]>0:
														return 'False'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[6]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=2:
										# {"feature": "Restaurant20to50", "instances": 59, "metric_value": 0.361, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Education", "instances": 56, "metric_value": 0.3497, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Children", "instances": 48, "metric_value": 0.3194, "depth": 12}
												if obj[5]>0:
													# {"feature": "Gender", "instances": 36, "metric_value": 0.3746, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Gender", "instances": 12, "metric_value": 0.1333, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>3:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.3571, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>2.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[11]>0:
							# {"feature": "Time", "instances": 556, "metric_value": 0.3922, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 451, "metric_value": 0.3659, "depth": 8}
								if obj[6]>1:
									# {"feature": "Restaurant20to50", "instances": 273, "metric_value": 0.3959, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Age", "instances": 157, "metric_value": 0.4229, "depth": 10}
										if obj[4]>1:
											# {"feature": "Children", "instances": 105, "metric_value": 0.4014, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 63, "metric_value": 0.4263, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Gender", "instances": 46, "metric_value": 0.469, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													# {"feature": "Gender", "instances": 17, "metric_value": 0.2567, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Bar", "instances": 42, "metric_value": 0.3347, "depth": 12}
												if obj[8]<=1.0:
													# {"feature": "Gender", "instances": 35, "metric_value": 0.3509, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>1.0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											# {"feature": "Bar", "instances": 52, "metric_value": 0.4354, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Gender", "instances": 30, "metric_value": 0.3873, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 21, "metric_value": 0.3627, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.4333, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												# {"feature": "Children", "instances": 22, "metric_value": 0.4886, "depth": 12}
												if obj[5]>0:
													# {"feature": "Gender", "instances": 14, "metric_value": 0.4898, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.3571, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1.0:
										# {"feature": "Bar", "instances": 116, "metric_value": 0.3455, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Children", "instances": 96, "metric_value": 0.3098, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Age", "instances": 67, "metric_value": 0.3515, "depth": 12}
												if obj[4]>1:
													# {"feature": "Gender", "instances": 36, "metric_value": 0.2487, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]<=1:
													# {"feature": "Gender", "instances": 31, "metric_value": 0.4367, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 29, "metric_value": 0.1552, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													# {"feature": "Age", "instances": 12, "metric_value": 0.3636, "depth": 13}
													if obj[4]<=3:
														return 'True'
													elif obj[4]>3:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Age", "instances": 20, "metric_value": 0.4484, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Children", "instances": 13, "metric_value": 0.4103, "depth": 12}
												if obj[5]>0:
													# {"feature": "Gender", "instances": 12, "metric_value": 0.4333, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Children", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[5]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=1:
									# {"feature": "Age", "instances": 178, "metric_value": 0.3119, "depth": 9}
									if obj[4]>0:
										# {"feature": "Bar", "instances": 161, "metric_value": 0.3267, "depth": 10}
										if obj[8]<=3.0:
											# {"feature": "Restaurant20to50", "instances": 155, "metric_value": 0.3162, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 132, "metric_value": 0.2974, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 74, "metric_value": 0.3045, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 58, "metric_value": 0.2807, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.4099, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 16, "metric_value": 0.375, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.4762, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>3.0:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.0882, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>1:
								# {"feature": "Restaurant20to50", "instances": 105, "metric_value": 0.4749, "depth": 8}
								if obj[10]<=2.0:
									# {"feature": "Education", "instances": 90, "metric_value": 0.4651, "depth": 9}
									if obj[6]<=3:
										# {"feature": "Children", "instances": 86, "metric_value": 0.4764, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Age", "instances": 55, "metric_value": 0.4836, "depth": 11}
											if obj[4]<=5:
												# {"feature": "Bar", "instances": 50, "metric_value": 0.4926, "depth": 12}
												if obj[8]<=1.0:
													# {"feature": "Gender", "instances": 29, "metric_value": 0.4932, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[8]>1.0:
													# {"feature": "Gender", "instances": 21, "metric_value": 0.4805, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>5:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 31, "metric_value": 0.4185, "depth": 11}
											if obj[3]>0:
												# {"feature": "Bar", "instances": 17, "metric_value": 0.2801, "depth": 12}
												if obj[8]<=1.0:
													# {"feature": "Age", "instances": 14, "metric_value": 0.2251, "depth": 13}
													if obj[4]<=4:
														return 'True'
													elif obj[4]>4:
														return 'True'
													else: return 'True'
												elif obj[8]>1.0:
													# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[4]<=0:
														return 'True'
													elif obj[4]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Age", "instances": 14, "metric_value": 0.381, "depth": 12}
												if obj[4]>0:
													# {"feature": "Bar", "instances": 12, "metric_value": 0.4333, "depth": 13}
													if obj[8]>0.0:
														return 'True'
													elif obj[8]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[4]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[6]>3:
										return 'True'
									else: return 'True'
								elif obj[10]>2.0:
									# {"feature": "Bar", "instances": 15, "metric_value": 0.3636, "depth": 9}
									if obj[8]>1.0:
										# {"feature": "Age", "instances": 11, "metric_value": 0.2727, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Education", "instances": 8, "metric_value": 0.3, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[6]>2:
												return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'True'
										else: return 'True'
									elif obj[8]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[7]>18.185882392956827:
						# {"feature": "Age", "instances": 119, "metric_value": 0.2638, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Education", "instances": 111, "metric_value": 0.2413, "depth": 7}
							if obj[6]>0:
								# {"feature": "Time", "instances": 71, "metric_value": 0.2853, "depth": 8}
								if obj[1]>0:
									# {"feature": "Gender", "instances": 51, "metric_value": 0.3153, "depth": 9}
									if obj[3]>0:
										# {"feature": "Bar", "instances": 36, "metric_value": 0.1852, "depth": 10}
										if obj[8]>0.0:
											return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Children", "instances": 15, "metric_value": 0.4286, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4857, "depth": 12}
												if obj[11]>0:
													# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Bar", "instances": 15, "metric_value": 0.3556, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Children", "instances": 12, "metric_value": 0.4167, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3571, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Bar", "instances": 20, "metric_value": 0.0857, "depth": 9}
									if obj[8]>0.0:
										return 'True'
									elif obj[8]<=0.0:
										# {"feature": "Children", "instances": 7, "metric_value": 0.1905, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]<=0:
								# {"feature": "Time", "instances": 40, "metric_value": 0.1234, "depth": 8}
								if obj[1]>0:
									# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.0547, "depth": 9}
									if obj[10]>0.0:
										return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Bar", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[8]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Children", "instances": 8, "metric_value": 0.3333, "depth": 9}
									if obj[5]>0:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>6:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[1]>1:
									# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=3.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=1:
									return 'True'
								else: return 'True'
							elif obj[11]>0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[1]>0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=3.0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 915, "metric_value": 0.3493, "depth": 5}
					if obj[8]<=3.0:
						# {"feature": "Time", "instances": 854, "metric_value": 0.3376, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Age", "instances": 516, "metric_value": 0.2995, "depth": 7}
							if obj[4]<=5:
								# {"feature": "Occupation", "instances": 443, "metric_value": 0.2772, "depth": 8}
								if obj[7]>1:
									# {"feature": "Restaurant20to50", "instances": 394, "metric_value": 0.2966, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Education", "instances": 360, "metric_value": 0.2768, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Gender", "instances": 333, "metric_value": 0.2989, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 168, "metric_value": 0.311, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 125, "metric_value": 0.2796, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4024, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 165, "metric_value": 0.2807, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 101, "metric_value": 0.3055, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 64, "metric_value": 0.2417, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>3:
											return 'True'
										else: return 'True'
									elif obj[10]>2.0:
										# {"feature": "Education", "instances": 34, "metric_value": 0.4452, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Children", "instances": 22, "metric_value": 0.4538, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.4231, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4815, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>2:
											# {"feature": "Children", "instances": 12, "metric_value": 0.25, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=1:
									# {"feature": "Education", "instances": 49, "metric_value": 0.0583, "depth": 9}
									if obj[6]<=2:
										return 'True'
									elif obj[6]>2:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2857, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>5:
								# {"feature": "Occupation", "instances": 73, "metric_value": 0.4002, "depth": 8}
								if obj[7]<=13:
									# {"feature": "Restaurant20to50", "instances": 69, "metric_value": 0.4148, "depth": 9}
									if obj[10]>1.0:
										# {"feature": "Children", "instances": 37, "metric_value": 0.3604, "depth": 10}
										if obj[5]>0:
											# {"feature": "Education", "instances": 25, "metric_value": 0.3, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 20, "metric_value": 0.2308, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.4, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 10, "metric_value": 0.4444, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=1.0:
										# {"feature": "Education", "instances": 32, "metric_value": 0.45, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4242, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 16, "metric_value": 0.3667, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.3961, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[6]>2:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[5]>0:
													return 'False'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[7]>13:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Age", "instances": 338, "metric_value": 0.3803, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Education", "instances": 199, "metric_value": 0.4276, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Occupation", "instances": 127, "metric_value": 0.3844, "depth": 9}
									if obj[7]>6:
										# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.3116, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 66, "metric_value": 0.3141, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 41, "metric_value": 0.2829, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.2975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.2659, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 25, "metric_value": 0.3476, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.2907, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[7]<=6:
										# {"feature": "Gender", "instances": 60, "metric_value": 0.4159, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.4754, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Children", "instances": 38, "metric_value": 0.4617, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4339, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.2368, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 12, "metric_value": 0.2593, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Occupation", "instances": 72, "metric_value": 0.4556, "depth": 9}
									if obj[7]<=9:
										# {"feature": "Restaurant20to50", "instances": 53, "metric_value": 0.4846, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 46, "metric_value": 0.4836, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 28, "metric_value": 0.4762, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 18, "metric_value": 0.4444, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[5]>0:
													return 'True'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[7]>9:
										# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.3158, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Children", "instances": 16, "metric_value": 0.3667, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.4167, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>2.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>3:
								# {"feature": "Restaurant20to50", "instances": 139, "metric_value": 0.2823, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Gender", "instances": 117, "metric_value": 0.2421, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 60, "metric_value": 0.3, "depth": 10}
										if obj[6]>1:
											# {"feature": "Occupation", "instances": 30, "metric_value": 0.3801, "depth": 11}
											if obj[7]<=7:
												# {"feature": "Children", "instances": 17, "metric_value": 0.2868, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3047, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[7]>7:
												# {"feature": "Children", "instances": 13, "metric_value": 0.4718, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[6]<=1:
											# {"feature": "Occupation", "instances": 30, "metric_value": 0.1727, "depth": 11}
											if obj[7]<=7:
												# {"feature": "Children", "instances": 22, "metric_value": 0.2318, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.255, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[7]>7:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Occupation", "instances": 57, "metric_value": 0.1496, "depth": 10}
										if obj[7]>3:
											# {"feature": "Education", "instances": 34, "metric_value": 0.232, "depth": 11}
											if obj[6]>1:
												# {"feature": "Children", "instances": 18, "metric_value": 0.0988, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[6]<=1:
												# {"feature": "Children", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=3:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]<=0.0:
									# {"feature": "Occupation", "instances": 22, "metric_value": 0.3697, "depth": 9}
									if obj[7]>5:
										# {"feature": "Gender", "instances": 12, "metric_value": 0.2593, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.1778, "depth": 11}
											if obj[6]>0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[6]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=5:
										# {"feature": "Education", "instances": 10, "metric_value": 0.3167, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.1667, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>3.0:
						# {"feature": "Time", "instances": 61, "metric_value": 0.4287, "depth": 6}
						if obj[1]>0:
							# {"feature": "Children", "instances": 49, "metric_value": 0.3987, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.4365, "depth": 8}
								if obj[10]<=2.0:
									# {"feature": "Age", "instances": 23, "metric_value": 0.3652, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 20, "metric_value": 0.4167, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 12, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Occupation", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=18:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>0:
												# {"feature": "Occupation", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=2:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Occupation", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[7]<=7:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[10]>2.0:
									# {"feature": "Age", "instances": 20, "metric_value": 0.4278, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 18, "metric_value": 0.4722, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 16, "metric_value": 0.4682, "depth": 11}
											if obj[6]>0:
												# {"feature": "Occupation", "instances": 11, "metric_value": 0.4628, "depth": 12}
												if obj[7]<=1:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[7]<=14:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[7]<=7:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Occupation", "instances": 12, "metric_value": 0.3333, "depth": 7}
							if obj[7]<=12:
								# {"feature": "Age", "instances": 8, "metric_value": 0.3333, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.2667, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[6]>2:
											# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=4.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]<=2:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>12:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[12]>2:
				# {"feature": "Age", "instances": 271, "metric_value": 0.4868, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Passanger", "instances": 232, "metric_value": 0.4871, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 223, "metric_value": 0.4918, "depth": 6}
						if obj[6]>1:
							# {"feature": "Occupation", "instances": 138, "metric_value": 0.4876, "depth": 7}
							if obj[7]<=16:
								# {"feature": "Bar", "instances": 122, "metric_value": 0.4891, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Restaurant20to50", "instances": 118, "metric_value": 0.4822, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Children", "instances": 108, "metric_value": 0.4945, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 76, "metric_value": 0.4829, "depth": 11}
											if obj[3]>0:
												# {"feature": "Time", "instances": 40, "metric_value": 0.4608, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4931, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Time", "instances": 36, "metric_value": 0.4375, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>1:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 32, "metric_value": 0.4403, "depth": 11}
											if obj[3]>0:
												# {"feature": "Time", "instances": 19, "metric_value": 0.4737, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Time", "instances": 13, "metric_value": 0.3287, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2975, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[10]>2.0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.1333, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[8]>3.0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[10]>1.0:
												return 'False'
											elif obj[10]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>16:
								# {"feature": "Children", "instances": 16, "metric_value": 0.3125, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Bar", "instances": 10, "metric_value": 0.4167, "depth": 9}
									if obj[8]>1.0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.2667, "depth": 10}
										if obj[1]>0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[10]>0.0:
											return 'False'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Occupation", "instances": 85, "metric_value": 0.4649, "depth": 7}
							if obj[7]>4:
								# {"feature": "Gender", "instances": 59, "metric_value": 0.481, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.4361, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Bar", "instances": 26, "metric_value": 0.4154, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Time", "instances": 16, "metric_value": 0.3, "depth": 11}
											if obj[1]>0:
												# {"feature": "Children", "instances": 15, "metric_value": 0.2909, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											# {"feature": "Children", "instances": 10, "metric_value": 0.3, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Time", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[10]>1.0:
										# {"feature": "Time", "instances": 8, "metric_value": 0.2083, "depth": 10}
										if obj[1]>0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Time", "instances": 25, "metric_value": 0.419, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.4698, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Children", "instances": 15, "metric_value": 0.4074, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 9, "metric_value": 0.3444, "depth": 12}
												if obj[8]<=1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]>1.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Bar", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]<=4:
								# {"feature": "Time", "instances": 26, "metric_value": 0.3615, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Bar", "instances": 20, "metric_value": 0.3059, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3451, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Children", "instances": 15, "metric_value": 0.3852, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.4167, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>2.0:
											return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Children", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>2.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						# {"feature": "Children", "instances": 9, "metric_value": 0.1111, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[4]>5:
					# {"feature": "Education", "instances": 39, "metric_value": 0.3199, "depth": 5}
					if obj[6]>0:
						# {"feature": "Bar", "instances": 29, "metric_value": 0.2188, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Occupation", "instances": 20, "metric_value": 0.075, "depth": 7}
							if obj[7]<=10:
								return 'False'
							elif obj[7]>10:
								# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[10]>1.0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]<=1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>1.0:
							# {"feature": "Children", "instances": 9, "metric_value": 0.1852, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.0, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]<=0:
						# {"feature": "Time", "instances": 10, "metric_value": 0.175, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Children", "instances": 8, "metric_value": 0.1875, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[7]<=6:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>6:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2244, "metric_value": 0.4571, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Children", "instances": 1582, "metric_value": 0.4359, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Education", "instances": 798, "metric_value": 0.4799, "depth": 4}
				if obj[6]>1:
					# {"feature": "Restaurant20to50", "instances": 413, "metric_value": 0.4416, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Passanger", "instances": 300, "metric_value": 0.4015, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 257, "metric_value": 0.3766, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Age", "instances": 160, "metric_value": 0.4152, "depth": 8}
								if obj[4]>1:
									# {"feature": "Gender", "instances": 95, "metric_value": 0.3518, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Occupation", "instances": 49, "metric_value": 0.3432, "depth": 10}
										if obj[7]>5:
											# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.2705, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Distance", "instances": 23, "metric_value": 0.3964, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3529, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[7]<=5:
											# {"feature": "Distance", "instances": 13, "metric_value": 0.3487, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.2857, "depth": 12}
												if obj[9]<=1.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[9]>1.0:
													return 'True'
												else: return 'True'
											elif obj[12]>2:
												# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]<=1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Occupation", "instances": 46, "metric_value": 0.2398, "depth": 10}
										if obj[7]>1:
											# {"feature": "Distance", "instances": 33, "metric_value": 0.3196, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.381, "depth": 12}
												if obj[9]<=1.0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.44, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2286, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.1455, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=1:
									# {"feature": "Occupation", "instances": 65, "metric_value": 0.4379, "depth": 9}
									if obj[7]<=14:
										# {"feature": "Distance", "instances": 50, "metric_value": 0.4669, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4611, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.322, "depth": 12}
												if obj[9]<=2.0:
													# {"feature": "Gender", "instances": 17, "metric_value": 0.3479, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[9]>2.0:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.4394, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.3818, "depth": 13}
													if obj[9]<=2.0:
														return 'False'
													elif obj[9]>2.0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[9]>1.0:
														return 'True'
													elif obj[9]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[12]>2:
											# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.3594, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.2, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>14:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.2182, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Distance", "instances": 11, "metric_value": 0.2727, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.3667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[9]>1.0:
														return 'False'
													elif obj[9]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[9]<=-1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>1:
								# {"feature": "Distance", "instances": 97, "metric_value": 0.2754, "depth": 8}
								if obj[12]<=1:
									# {"feature": "Occupation", "instances": 71, "metric_value": 0.3352, "depth": 9}
									if obj[7]<=19:
										# {"feature": "Age", "instances": 65, "metric_value": 0.3124, "depth": 10}
										if obj[4]>2:
											# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.3739, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Gender", "instances": 19, "metric_value": 0.427, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[9]>0.0:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.3016, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=2:
											# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.1956, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.381, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>19:
										# {"feature": "Age", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]>0.0:
												return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[12]>1:
									# {"feature": "Direction_same", "instances": 26, "metric_value": 0.0659, "depth": 9}
									if obj[11]<=0:
										return 'False'
									elif obj[11]>0:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.1429, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[9]>0.0:
												return 'False'
											elif obj[9]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Age", "instances": 43, "metric_value": 0.4605, "depth": 7}
							if obj[4]>0:
								# {"feature": "Occupation", "instances": 35, "metric_value": 0.448, "depth": 8}
								if obj[7]>4:
									# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.4147, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Gender", "instances": 19, "metric_value": 0.3383, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Time", "instances": 14, "metric_value": 0.4429, "depth": 11}
											if obj[1]>2:
												# {"feature": "Distance", "instances": 10, "metric_value": 0.4167, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=2:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>3:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]<=4:
									# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.3, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[1]<=3:
												return 'True'
											elif obj[1]>3:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]>2.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]<=0:
								# {"feature": "Time", "instances": 8, "metric_value": 0.2143, "depth": 8}
								if obj[1]>2:
									# {"feature": "Occupation", "instances": 7, "metric_value": 0.1429, "depth": 9}
									if obj[7]<=10:
										return 'False'
									elif obj[7]>10:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[12]<=1:
											return 'False'
										elif obj[12]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[1]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[10]>1.0:
						# {"feature": "Coffeehouse", "instances": 113, "metric_value": 0.4621, "depth": 6}
						if obj[9]<=3.0:
							# {"feature": "Occupation", "instances": 97, "metric_value": 0.4611, "depth": 7}
							if obj[7]<=7:
								# {"feature": "Age", "instances": 63, "metric_value": 0.4713, "depth": 8}
								if obj[4]>1:
									# {"feature": "Time", "instances": 33, "metric_value": 0.4538, "depth": 9}
									if obj[1]>0:
										# {"feature": "Passanger", "instances": 21, "metric_value": 0.4222, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4074, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4167, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4667, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[12]<=2:
													return 'False'
												elif obj[12]>2:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Gender", "instances": 12, "metric_value": 0.3611, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[11]>0:
												return 'True'
											elif obj[11]<=0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[0]>0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.0, "depth": 11}
											if obj[11]<=0:
												return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=1:
									# {"feature": "Time", "instances": 30, "metric_value": 0.4444, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Passanger", "instances": 24, "metric_value": 0.471, "depth": 10}
										if obj[0]>0:
											# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4783, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Distance", "instances": 14, "metric_value": 0.4848, "depth": 12}
												if obj[12]>1:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.4545, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4167, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.4583, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>3:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[12]<=1:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[0]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>0:
												return 'False'
											else: return 'False'
										elif obj[12]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>7:
								# {"feature": "Gender", "instances": 34, "metric_value": 0.3548, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Distance", "instances": 23, "metric_value": 0.2609, "depth": 9}
									if obj[12]<=2:
										# {"feature": "Age", "instances": 16, "metric_value": 0.3462, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3692, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Passanger", "instances": 10, "metric_value": 0.475, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Time", "instances": 8, "metric_value": 0.3571, "depth": 13}
													if obj[1]<=2:
														return 'True'
													elif obj[1]>2:
														return 'False'
													else: return 'False'
												elif obj[0]>1:
													# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[1]<=2:
														return 'False'
													elif obj[1]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										elif obj[4]>4:
											return 'True'
										else: return 'True'
									elif obj[12]>2:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									# {"feature": "Time", "instances": 11, "metric_value": 0.3636, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.3333, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Passanger", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[0]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[0]>0:
													return 'True'
												else: return 'True'
											elif obj[12]>2:
												# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[9]>3.0:
							# {"feature": "Distance", "instances": 16, "metric_value": 0.2625, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Time", "instances": 10, "metric_value": 0.3429, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Age", "instances": 7, "metric_value": 0.4048, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[0]>0:
											return 'False'
										elif obj[0]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[7]<=20:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>2:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[11]<=0:
												return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							elif obj[12]>2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=1:
					# {"feature": "Occupation", "instances": 385, "metric_value": 0.4852, "depth": 5}
					if obj[7]>4:
						# {"feature": "Restaurant20to50", "instances": 282, "metric_value": 0.4904, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Distance", "instances": 278, "metric_value": 0.4924, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Age", "instances": 231, "metric_value": 0.4856, "depth": 8}
								if obj[4]<=5:
									# {"feature": "Coffeehouse", "instances": 205, "metric_value": 0.4931, "depth": 9}
									if obj[9]>-1.0:
										# {"feature": "Passanger", "instances": 203, "metric_value": 0.4947, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 155, "metric_value": 0.4967, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Gender", "instances": 130, "metric_value": 0.4986, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 78, "metric_value": 0.4986, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 52, "metric_value": 0.4957, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[1]>3:
												# {"feature": "Gender", "instances": 25, "metric_value": 0.4778, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]<=0:
											# {"feature": "Gender", "instances": 48, "metric_value": 0.428, "depth": 11}
											if obj[3]>0:
												# {"feature": "Time", "instances": 34, "metric_value": 0.395, "depth": 12}
												if obj[1]>2:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4753, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=2:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3047, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Time", "instances": 14, "metric_value": 0.4048, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]>2:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[4]>5:
									# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.3262, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Time", "instances": 19, "metric_value": 0.1689, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Passanger", "instances": 16, "metric_value": 0.1, "depth": 11}
											if obj[0]<=1:
												return 'True'
											elif obj[0]>1:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>3:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[0]>0:
												return 'False'
											elif obj[0]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]>2.0:
										# {"feature": "Passanger", "instances": 7, "metric_value": 0.381, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 6, "metric_value": 0.3333, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]>2:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[12]>2:
								# {"feature": "Coffeehouse", "instances": 47, "metric_value": 0.4439, "depth": 8}
								if obj[9]<=3.0:
									# {"feature": "Age", "instances": 44, "metric_value": 0.4523, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Passanger", "instances": 41, "metric_value": 0.4796, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 37, "metric_value": 0.4884, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 29, "metric_value": 0.4814, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]<=0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[0]<=0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[3]>0:
												# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>6:
										return 'False'
									else: return 'False'
								elif obj[9]>3.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[10]>2.0:
							return 'True'
						else: return 'True'
					elif obj[7]<=4:
						# {"feature": "Age", "instances": 103, "metric_value": 0.4052, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Passanger", "instances": 75, "metric_value": 0.3551, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 63, "metric_value": 0.3131, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.1922, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.1905, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 28, "metric_value": 0.2429, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 17, "metric_value": 0.1925, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.297, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 11, "metric_value": 0.2803, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'False'
										else: return 'False'
									elif obj[10]>2.0:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 26, "metric_value": 0.3877, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Distance", "instances": 25, "metric_value": 0.36, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.35, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.3882, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Gender", "instances": 17, "metric_value": 0.4504, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										elif obj[12]>2:
											return 'True'
										else: return 'True'
									elif obj[11]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.4, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.4, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.4333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[10]>1.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[10]<=0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>3:
										return 'False'
									else: return 'False'
								elif obj[9]>2.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>5:
							# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.352, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.3571, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.375, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.3571, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							elif obj[9]>1.0:
								# {"feature": "Distance", "instances": 14, "metric_value": 0.2024, "depth": 8}
								if obj[12]<=2:
									# {"feature": "Time", "instances": 12, "metric_value": 0.1111, "depth": 9}
									if obj[1]<=3:
										return 'True'
									elif obj[1]>3:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[12]>2:
									# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[5]>0:
				# {"feature": "Time", "instances": 784, "metric_value": 0.3736, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coffeehouse", "instances": 680, "metric_value": 0.4004, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Occupation", "instances": 546, "metric_value": 0.4215, "depth": 6}
						if obj[7]>1.3126861298204782:
							# {"feature": "Restaurant20to50", "instances": 421, "metric_value": 0.4458, "depth": 7}
							if obj[10]<=2.0:
								# {"feature": "Passanger", "instances": 389, "metric_value": 0.436, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Age", "instances": 332, "metric_value": 0.4211, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Education", "instances": 230, "metric_value": 0.444, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Direction_same", "instances": 221, "metric_value": 0.4514, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Distance", "instances": 159, "metric_value": 0.4636, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Gender", "instances": 108, "metric_value": 0.4792, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													# {"feature": "Gender", "instances": 51, "metric_value": 0.4304, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Distance", "instances": 62, "metric_value": 0.4093, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Gender", "instances": 41, "metric_value": 0.419, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													# {"feature": "Gender", "instances": 21, "metric_value": 0.3492, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>3:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.1778, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>3:
										# {"feature": "Direction_same", "instances": 102, "metric_value": 0.3542, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Education", "instances": 74, "metric_value": 0.3185, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Distance", "instances": 70, "metric_value": 0.3324, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Gender", "instances": 49, "metric_value": 0.3691, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													# {"feature": "Gender", "instances": 21, "metric_value": 0.1786, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>3:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Gender", "instances": 28, "metric_value": 0.422, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 15, "metric_value": 0.4571, "depth": 12}
												if obj[6]>0:
													# {"feature": "Distance", "instances": 14, "metric_value": 0.4762, "depth": 13}
													if obj[12]<=1:
														return 'True'
													elif obj[12]>1:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 13, "metric_value": 0.3192, "depth": 12}
												if obj[6]>0:
													# {"feature": "Distance", "instances": 8, "metric_value": 0.1875, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													# {"feature": "Distance", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]>2:
									# {"feature": "Education", "instances": 57, "metric_value": 0.4413, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Age", "instances": 42, "metric_value": 0.3956, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Gender", "instances": 39, "metric_value": 0.4258, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4339, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 22, "metric_value": 0.4339, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 17, "metric_value": 0.4152, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									elif obj[6]>2:
										# {"feature": "Age", "instances": 15, "metric_value": 0.3744, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.3077, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>6:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[10]>2.0:
								# {"feature": "Age", "instances": 32, "metric_value": 0.3385, "depth": 8}
								if obj[4]>2:
									# {"feature": "Distance", "instances": 20, "metric_value": 0.3214, "depth": 9}
									if obj[12]>1:
										# {"feature": "Passanger", "instances": 14, "metric_value": 0.3155, "depth": 10}
										if obj[0]>1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.125, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=4:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]<=1:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[6]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[12]<=1:
										return 'True'
									else: return 'True'
								elif obj[4]<=2:
									# {"feature": "Passanger", "instances": 12, "metric_value": 0.2593, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Distance", "instances": 9, "metric_value": 0.2963, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.3333, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=3:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[12]>2:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]<=1.3126861298204782:
							# {"feature": "Education", "instances": 125, "metric_value": 0.2852, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Restaurant20to50", "instances": 111, "metric_value": 0.2478, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Age", "instances": 89, "metric_value": 0.3018, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Direction_same", "instances": 73, "metric_value": 0.3337, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Distance", "instances": 55, "metric_value": 0.281, "depth": 11}
											if obj[12]>1:
												# {"feature": "Passanger", "instances": 44, "metric_value": 0.2328, "depth": 12}
												if obj[0]>0:
													# {"feature": "Gender", "instances": 41, "metric_value": 0.2465, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													return 'False'
												else: return 'False'
											elif obj[12]<=1:
												# {"feature": "Passanger", "instances": 11, "metric_value": 0.3939, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												elif obj[0]>1:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Passanger", "instances": 18, "metric_value": 0.2667, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.32, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Distance", "instances": 15, "metric_value": 0.32, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>4:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.1111, "depth": 10}
										if obj[12]>1:
											# {"feature": "Passanger", "instances": 9, "metric_value": 0.1852, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										elif obj[12]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[6]>2:
								# {"feature": "Age", "instances": 14, "metric_value": 0.3896, "depth": 8}
								if obj[4]>0:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.3636, "depth": 9}
									if obj[12]<=2:
										# {"feature": "Passanger", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3333, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[0]>2:
											return 'True'
										else: return 'True'
									elif obj[12]>2:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>2.0:
						# {"feature": "Direction_same", "instances": 134, "metric_value": 0.2719, "depth": 6}
						if obj[11]<=0:
							# {"feature": "Age", "instances": 102, "metric_value": 0.2135, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Education", "instances": 80, "metric_value": 0.2657, "depth": 8}
								if obj[6]>0:
									# {"feature": "Occupation", "instances": 66, "metric_value": 0.2264, "depth": 9}
									if obj[7]>5:
										# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.3067, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Gender", "instances": 30, "metric_value": 0.3457, "depth": 11}
											if obj[3]>0:
												# {"feature": "Passanger", "instances": 27, "metric_value": 0.3704, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Distance", "instances": 15, "metric_value": 0.4074, "depth": 13}
													if obj[12]<=2:
														return 'False'
													elif obj[12]>2:
														return 'False'
													else: return 'False'
												elif obj[0]>1:
													# {"feature": "Distance", "instances": 12, "metric_value": 0.2727, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]>2.0:
											return 'False'
										else: return 'False'
									elif obj[7]<=5:
										# {"feature": "Gender", "instances": 31, "metric_value": 0.1136, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 26, "metric_value": 0.0705, "depth": 11}
											if obj[0]<=1:
												return 'False'
											elif obj[0]>1:
												# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.15, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Distance", "instances": 10, "metric_value": 0.175, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[12]<=2:
												return 'False'
											elif obj[12]>2:
												# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=0:
									# {"feature": "Passanger", "instances": 14, "metric_value": 0.3714, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Occupation", "instances": 10, "metric_value": 0.24, "depth": 10}
										if obj[7]<=6:
											return 'False'
										elif obj[7]>6:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Occupation", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[7]<=4:
											return 'True'
										elif obj[7]>4:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[4]>3:
								return 'False'
							else: return 'False'
						elif obj[11]>0:
							# {"feature": "Age", "instances": 32, "metric_value": 0.3952, "depth": 7}
							if obj[4]>2:
								# {"feature": "Passanger", "instances": 19, "metric_value": 0.4211, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4286, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Education", "instances": 14, "metric_value": 0.3869, "depth": 10}
										if obj[6]>2:
											# {"feature": "Occupation", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[7]<=7:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Distance", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[7]>7:
												return 'True'
											else: return 'True'
										elif obj[6]<=2:
											# {"feature": "Occupation", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[7]>7:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											elif obj[7]<=7:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>2.0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								# {"feature": "Occupation", "instances": 13, "metric_value": 0.1538, "depth": 8}
								if obj[7]>1:
									return 'False'
								elif obj[7]<=1:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[10]>1.0:
										return 'False'
									elif obj[10]<=1.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Passanger", "instances": 104, "metric_value": 0.1315, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Gender", "instances": 99, "metric_value": 0.1094, "depth": 6}
						if obj[3]>0:
							# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.0, "depth": 7}
							if obj[10]<=2.0:
								return 'False'
							elif obj[10]>2.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 44, "metric_value": 0.1804, "depth": 7}
							if obj[7]>4:
								# {"feature": "Coffeehouse", "instances": 39, "metric_value": 0.1329, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Education", "instances": 22, "metric_value": 0.2216, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Age", "instances": 16, "metric_value": 0.2636, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.1455, "depth": 11}
											if obj[10]<=1.0:
												return 'False'
											elif obj[10]>1.0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>2:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[10]>1.0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[12]>1:
													return 'False'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]>2:
										return 'False'
									else: return 'False'
								elif obj[9]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[7]<=4:
								# {"feature": "Education", "instances": 5, "metric_value": 0.2667, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								elif obj[6]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.0, "depth": 6}
						if obj[7]<=11:
							return 'True'
						elif obj[7]>11:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			# {"feature": "Restaurant20to50", "instances": 662, "metric_value": 0.4594, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Passanger", "instances": 355, "metric_value": 0.4904, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 290, "metric_value": 0.4838, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Occupation", "instances": 202, "metric_value": 0.4801, "depth": 6}
						if obj[7]<=13.60630442015693:
							# {"feature": "Gender", "instances": 170, "metric_value": 0.4739, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Children", "instances": 102, "metric_value": 0.4309, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Direction_same", "instances": 73, "metric_value": 0.4735, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Coffeehouse", "instances": 47, "metric_value": 0.4566, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Age", "instances": 30, "metric_value": 0.4196, "depth": 11}
											if obj[4]>2:
												# {"feature": "Distance", "instances": 16, "metric_value": 0.45, "depth": 12}
												if obj[12]>1:
													# {"feature": "Education", "instances": 15, "metric_value": 0.4786, "depth": 13}
													if obj[6]>0:
														return 'True'
													elif obj[6]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											elif obj[4]<=2:
												# {"feature": "Education", "instances": 14, "metric_value": 0.2857, "depth": 12}
												if obj[6]>1:
													# {"feature": "Distance", "instances": 9, "metric_value": 0.4, "depth": 13}
													if obj[12]>2:
														return 'False'
													elif obj[12]<=2:
														return 'False'
													else: return 'False'
												elif obj[6]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>2.0:
											# {"feature": "Distance", "instances": 17, "metric_value": 0.2941, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Education", "instances": 10, "metric_value": 0.375, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Age", "instances": 8, "metric_value": 0.3571, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													return 'True'
												else: return 'True'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>0:
										# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.3419, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Education", "instances": 18, "metric_value": 0.4167, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Distance", "instances": 16, "metric_value": 0.4167, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Age", "instances": 15, "metric_value": 0.4286, "depth": 13}
													if obj[4]<=4:
														return 'True'
													elif obj[4]>4:
														return 'True'
													else: return 'True'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											elif obj[6]>2:
												return 'False'
											else: return 'False'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>0:
									# {"feature": "Age", "instances": 29, "metric_value": 0.2371, "depth": 9}
									if obj[4]>2:
										# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.3021, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Distance", "instances": 12, "metric_value": 0.25, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Education", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[6]<=1:
												return 'False'
											elif obj[6]>1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Education", "instances": 68, "metric_value": 0.4834, "depth": 8}
								if obj[6]>1:
									# {"feature": "Age", "instances": 37, "metric_value": 0.4142, "depth": 9}
									if obj[4]>1:
										# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.4076, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Distance", "instances": 25, "metric_value": 0.3726, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Children", "instances": 19, "metric_value": 0.3088, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3905, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[12]>2:
												# {"feature": "Children", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[9]<=0.0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[12]<=2:
												return 'True'
											elif obj[12]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.2667, "depth": 10}
										if obj[9]<=0.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										elif obj[9]>0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=1:
									# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.3829, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Distance", "instances": 23, "metric_value": 0.3794, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Age", "instances": 17, "metric_value": 0.4059, "depth": 11}
											if obj[4]>1:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.3429, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.2286, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[4]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]>2:
											# {"feature": "Age", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[4]>1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.3, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=1:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[7]>13.60630442015693:
							# {"feature": "Age", "instances": 32, "metric_value": 0.4167, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Distance", "instances": 20, "metric_value": 0.2637, "depth": 8}
								if obj[12]>1:
									# {"feature": "Education", "instances": 13, "metric_value": 0.1154, "depth": 9}
									if obj[6]<=2:
										return 'False'
									elif obj[6]>2:
										# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[5]>0:
											return 'False'
										elif obj[5]<=0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[9]>0.0:
												return 'True'
											elif obj[9]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[12]<=1:
									# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.3429, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[6]>0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>2:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.2381, "depth": 8}
								if obj[12]<=2:
									# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2857, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[11]>0:
											return 'True'
										elif obj[11]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[12]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]>2:
						# {"feature": "Gender", "instances": 88, "metric_value": 0.4489, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Age", "instances": 59, "metric_value": 0.4039, "depth": 7}
							if obj[4]>0:
								# {"feature": "Direction_same", "instances": 44, "metric_value": 0.4242, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Occupation", "instances": 42, "metric_value": 0.4228, "depth": 9}
									if obj[7]<=21:
										# {"feature": "Coffeehouse", "instances": 41, "metric_value": 0.4138, "depth": 10}
										if obj[9]<=3.0:
											# {"feature": "Distance", "instances": 38, "metric_value": 0.3907, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Education", "instances": 21, "metric_value": 0.4571, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Children", "instances": 20, "metric_value": 0.4714, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													return 'False'
												else: return 'False'
											elif obj[12]>1:
												# {"feature": "Children", "instances": 17, "metric_value": 0.2353, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Education", "instances": 9, "metric_value": 0.4167, "depth": 13}
													if obj[6]<=2:
														return 'False'
													elif obj[6]>2:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>3.0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[12]<=1:
													return 'False'
												elif obj[12]>1:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>21:
										return 'True'
									else: return 'True'
								elif obj[11]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								# {"feature": "Children", "instances": 15, "metric_value": 0.2, "depth": 8}
								if obj[5]>0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3333, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[6]<=2:
											return 'False'
										elif obj[6]>2:
											# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[12]>1:
												return 'True'
											elif obj[12]<=1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[11]>0:
										# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[6]>2:
											return 'False'
										elif obj[6]<=2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>0:
							# {"feature": "Age", "instances": 29, "metric_value": 0.4263, "depth": 7}
							if obj[4]>1:
								# {"feature": "Occupation", "instances": 18, "metric_value": 0.4167, "depth": 8}
								if obj[7]<=5:
									# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.35, "depth": 9}
									if obj[9]<=3.0:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.24, "depth": 10}
										if obj[12]<=1:
											return 'False'
										elif obj[12]>1:
											# {"feature": "Education", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[6]>1:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>3.0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[12]<=1:
											return 'True'
										elif obj[12]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]>5:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[5]>0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[12]>1:
													return 'True'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[12]>1:
													return 'False'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[6]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Education", "instances": 11, "metric_value": 0.2909, "depth": 8}
								if obj[6]<=4:
									# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.1778, "depth": 9}
									if obj[9]>-1.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1111, "depth": 10}
										if obj[11]<=0:
											return 'True'
										elif obj[11]>0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[7]<=4:
												return 'False'
											elif obj[7]>4:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[6]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 65, "metric_value": 0.4117, "depth": 5}
					if obj[1]>2:
						# {"feature": "Age", "instances": 47, "metric_value": 0.3245, "depth": 6}
						if obj[4]>1:
							# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.4196, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Children", "instances": 20, "metric_value": 0.44, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Occupation", "instances": 15, "metric_value": 0.4308, "depth": 9}
									if obj[7]>2:
										# {"feature": "Education", "instances": 13, "metric_value": 0.4249, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[6]>0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													elif obj[12]>1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=2:
										return 'True'
									else: return 'True'
								elif obj[5]>0:
									# {"feature": "Education", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[6]<=0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[7]>15:
												return 'False'
											elif obj[7]<=15:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[6]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]>2.0:
								# {"feature": "Gender", "instances": 8, "metric_value": 0.125, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=1:
							# {"feature": "Occupation", "instances": 19, "metric_value": 0.0877, "depth": 7}
							if obj[7]>1:
								return 'True'
							elif obj[7]<=1:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.1667, "depth": 8}
								if obj[9]>0.0:
									return 'True'
								elif obj[9]<=0.0:
									# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=2:
						# {"feature": "Occupation", "instances": 18, "metric_value": 0.2564, "depth": 6}
						if obj[7]<=10:
							# {"feature": "Age", "instances": 13, "metric_value": 0.3077, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.3333, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]>2:
										return 'False'
									else: return 'False'
								elif obj[9]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						elif obj[7]>10:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[10]>1.0:
				# {"feature": "Direction_same", "instances": 307, "metric_value": 0.4012, "depth": 4}
				if obj[11]<=0:
					# {"feature": "Education", "instances": 250, "metric_value": 0.4308, "depth": 5}
					if obj[6]>1:
						# {"feature": "Occupation", "instances": 161, "metric_value": 0.4573, "depth": 6}
						if obj[7]>1:
							# {"feature": "Children", "instances": 133, "metric_value": 0.4695, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Time", "instances": 93, "metric_value": 0.4866, "depth": 8}
								if obj[1]>2:
									# {"feature": "Gender", "instances": 51, "metric_value": 0.4647, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 32, "metric_value": 0.3823, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Passanger", "instances": 20, "metric_value": 0.2637, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.1319, "depth": 12}
												if obj[9]>2.0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.2143, "depth": 13}
													if obj[12]<=1:
														return 'True'
													elif obj[12]>1:
														return 'True'
													else: return 'True'
												elif obj[9]<=2.0:
													return 'True'
												else: return 'True'
											elif obj[0]>1:
												# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[9]<=3.0:
													# {"feature": "Distance", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												elif obj[9]>3.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Passanger", "instances": 12, "metric_value": 0.3611, "depth": 11}
											if obj[0]>1:
												# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.0, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[0]<=1:
												# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Distance", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[12]<=1:
														return 'False'
													else: return 'False'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Passanger", "instances": 19, "metric_value": 0.4298, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.3889, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Age", "instances": 12, "metric_value": 0.4444, "depth": 12}
												if obj[4]>1:
													# {"feature": "Distance", "instances": 9, "metric_value": 0.4167, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'False'
													else: return 'False'
												elif obj[4]<=1:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[4]>0:
												return 'True'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[1]<=2:
									# {"feature": "Distance", "instances": 42, "metric_value": 0.463, "depth": 9}
									if obj[12]>1:
										# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.4618, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 22, "metric_value": 0.4211, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Age", "instances": 13, "metric_value": 0.4256, "depth": 12}
												if obj[4]>1:
													# {"feature": "Passanger", "instances": 10, "metric_value": 0.4, "depth": 13}
													if obj[0]>0:
														return 'False'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]<=1:
													# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[0]<=1:
														return 'True'
													elif obj[0]>1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Age", "instances": 9, "metric_value": 0.3016, "depth": 12}
												if obj[4]>0:
													# {"feature": "Passanger", "instances": 7, "metric_value": 0.2381, "depth": 13}
													if obj[0]>0:
														return 'True'
													elif obj[0]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]<=0:
													# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[0]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											# {"feature": "Gender", "instances": 14, "metric_value": 0.3673, "depth": 11}
											if obj[3]>0:
												# {"feature": "Age", "instances": 7, "metric_value": 0.1905, "depth": 12}
												if obj[4]>0:
													return 'False'
												elif obj[4]<=0:
													# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[0]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Age", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Passanger", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[0]>0:
														return 'False'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]>1:
													# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[0]>0:
														return 'False'
													elif obj[0]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[12]<=1:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[5]>0:
								# {"feature": "Age", "instances": 40, "metric_value": 0.3273, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Passanger", "instances": 21, "metric_value": 0.1534, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Distance", "instances": 18, "metric_value": 0.0889, "depth": 10}
										if obj[12]<=2:
											return 'True'
										elif obj[12]>2:
											# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[1]>0:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]>2:
										# {"feature": "Time", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[1]<=3:
											return 'True'
										elif obj[1]>3:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>2:
									# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.3322, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.1778, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Distance", "instances": 9, "metric_value": 0.1852, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Passanger", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												elif obj[0]>1:
													return 'True'
												else: return 'True'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										elif obj[1]>3:
											return 'False'
										else: return 'False'
									elif obj[9]<=1.0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.1481, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[1]>0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[12]>2:
													return 'True'
												elif obj[12]<=2:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=1:
							# {"feature": "Passanger", "instances": 28, "metric_value": 0.2434, "depth": 7}
							if obj[0]>0:
								# {"feature": "Distance", "instances": 27, "metric_value": 0.2339, "depth": 8}
								if obj[12]<=2:
									# {"feature": "Time", "instances": 19, "metric_value": 0.2551, "depth": 9}
									if obj[1]>1:
										# {"feature": "Gender", "instances": 13, "metric_value": 0.1154, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[9]<=4.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=1:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[9]<=2.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[12]>2:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]<=1:
						# {"feature": "Occupation", "instances": 89, "metric_value": 0.3213, "depth": 6}
						if obj[7]<=10:
							# {"feature": "Age", "instances": 53, "metric_value": 0.3821, "depth": 7}
							if obj[4]>1:
								# {"feature": "Passanger", "instances": 27, "metric_value": 0.4807, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Children", "instances": 23, "metric_value": 0.4842, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.4078, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Time", "instances": 12, "metric_value": 0.3704, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.3175, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.3714, "depth": 13}
													if obj[12]<=2:
														return 'True'
													elif obj[12]>2:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[12]<=2:
												return 'False'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[3]<=0:
											return 'False'
										elif obj[3]>0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[1]<=1:
												return 'True'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[0]>2:
									# {"feature": "Time", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[1]>2:
										return 'True'
									elif obj[1]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Passanger", "instances": 26, "metric_value": 0.2168, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.1455, "depth": 9}
									if obj[9]<=1.0:
										return 'True'
									elif obj[9]>1.0:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.2857, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Time", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[1]>1:
													# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=1:
													return 'True'
												else: return 'True'
											elif obj[12]>2:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>10:
							# {"feature": "Age", "instances": 36, "metric_value": 0.1212, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								# {"feature": "Children", "instances": 11, "metric_value": 0.2727, "depth": 8}
								if obj[5]>0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[12]<=2:
											return 'False'
										elif obj[12]>2:
											return 'True'
										else: return 'True'
									elif obj[0]>2:
										return 'True'
									else: return 'True'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[11]>0:
					# {"feature": "Time", "instances": 57, "metric_value": 0.2047, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Age", "instances": 40, "metric_value": 0.1086, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Occupation", "instances": 35, "metric_value": 0.0286, "depth": 7}
							if obj[7]<=21:
								return 'True'
							elif obj[7]>21:
								# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>5:
							# {"feature": "Occupation", "instances": 5, "metric_value": 0.2667, "depth": 7}
							if obj[7]<=12:
								# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[5]<=0:
									return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[7]>12:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]>0:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.2834, "depth": 6}
						if obj[12]>1:
							# {"feature": "Age", "instances": 11, "metric_value": 0.1364, "depth": 7}
							if obj[4]<=3:
								return 'True'
							elif obj[4]>3:
								# {"feature": "Education", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[12]<=1:
							# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[7]>5:
									return 'True'
								elif obj[7]<=5:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[4]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[9]<=2.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
