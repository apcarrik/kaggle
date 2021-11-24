def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 98, "metric_value": 0.9952, "depth": 2}
		if obj[8]<=3:
			# {"feature": "Direction_same", "instances": 91, "metric_value": 0.9852, "depth": 3}
			if obj[14]<=0:
				# {"feature": "Age", "instances": 65, "metric_value": 0.9501, "depth": 4}
				if obj[6]>0:
					# {"feature": "Restaurant20to50", "instances": 53, "metric_value": 0.9791, "depth": 5}
					if obj[13]>0.0:
						# {"feature": "Time", "instances": 45, "metric_value": 0.9968, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Children", "instances": 41, "metric_value": 0.9789, "depth": 7}
							if obj[7]>0:
								# {"feature": "Gender", "instances": 21, "metric_value": 0.8631, "depth": 8}
								if obj[5]>0:
									# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 9}
									if obj[3]>0:
										# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[9]>1:
											# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 11}
											if obj[10]>2:
												# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[1]<=0:
													return 'False'
												elif obj[1]>0:
													# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[4]>0:
														return 'True'
													elif obj[4]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[10]<=2:
												# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[4]>0:
													# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[12]>-1.0:
														return 'False'
													elif obj[12]<=-1.0:
														return 'True'
													else: return 'True'
												elif obj[4]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[5]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=0:
								# {"feature": "Distance", "instances": 20, "metric_value": 0.9928, "depth": 8}
								if obj[15]>1:
									# {"feature": "Weather", "instances": 14, "metric_value": 0.9403, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 10}
										if obj[10]<=4:
											# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 11}
											if obj[3]>0:
												# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[9]<=7:
													# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[11]<=1.0:
														# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[12]>0.0:
															# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[4]>0:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[5]<=0:
																	return 'False'
																elif obj[5]>0:
																	return 'True'
																else: return 'True'
															elif obj[4]<=0:
																return 'False'
															else: return 'False'
														elif obj[12]<=0.0:
															return 'True'
														else: return 'True'
													elif obj[11]>1.0:
														return 'False'
													else: return 'False'
												elif obj[9]>7:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]>4:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[15]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[13]<=0.0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[9]<=11:
							return 'False'
						elif obj[9]>11:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=0:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[12]>0.0:
						return 'False'
					elif obj[12]<=0.0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>2:
							# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[9]<=10:
								return 'False'
							elif obj[9]>10:
								return 'True'
							else: return 'True'
						elif obj[3]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[14]>0:
				# {"feature": "Time", "instances": 26, "metric_value": 0.9829, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[9]>3:
						# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[11]<=3.0:
							return 'True'
						elif obj[11]>3.0:
							return 'False'
						else: return 'False'
					elif obj[9]<=3:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>1:
							return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>1:
					# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=3:
						return 'False'
					elif obj[6]>3:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]>5:
							return 'True'
						elif obj[9]<=5:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[8]>3:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[9]<=21:
				return 'True'
			elif obj[9]>21:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coupon_validity", "instances": 29, "metric_value": 0.5788, "depth": 2}
		if obj[4]<=0:
			return 'True'
		elif obj[4]>0:
			# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[8]<=3:
				# {"feature": "Income", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[10]<=6:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>2:
							return 'True'
						elif obj[2]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]>6:
					return 'False'
				else: return 'False'
			elif obj[8]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
