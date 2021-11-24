def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Income", "instances": 113, "metric_value": 0.9904, "depth": 1}
	if obj[13]<=6:
		# {"feature": "Coupon", "instances": 97, "metric_value": 0.9999, "depth": 2}
		if obj[5]>0:
			# {"feature": "Distance", "instances": 81, "metric_value": 0.9911, "depth": 3}
			if obj[20]<=2:
				# {"feature": "Coffeehouse", "instances": 74, "metric_value": 0.974, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Maritalstatus", "instances": 58, "metric_value": 0.9966, "depth": 5}
					if obj[9]<=2:
						# {"feature": "Passanger", "instances": 54, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							# {"feature": "Bar", "instances": 51, "metric_value": 0.9975, "depth": 7}
							if obj[14]>-1.0:
								# {"feature": "Children", "instances": 49, "metric_value": 0.9925, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.9972, "depth": 9}
									if obj[18]>0.0:
										# {"feature": "Age", "instances": 24, "metric_value": 0.9544, "depth": 10}
										if obj[8]<=4:
											# {"feature": "Gender", "instances": 20, "metric_value": 0.9928, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 12}
												if obj[12]>5:
													# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[0]<=1:
														# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[6]<=0:
															return 'True'
														elif obj[6]>0:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]<=55:
																return 'False'
															elif obj[3]>55:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[0]>1:
														return 'False'
													else: return 'False'
												elif obj[12]<=5:
													return 'False'
												else: return 'False'
											elif obj[7]>0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 12}
												if obj[19]<=0:
													return 'True'
												elif obj[19]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>4:
											return 'True'
										else: return 'True'
									elif obj[18]<=0.0:
										# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[3]>55:
												# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[4]<=0:
													# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[6]<=0:
														return 'False'
													elif obj[6]>0:
														return 'True'
													else: return 'True'
												elif obj[4]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=55:
												return 'True'
											else: return 'True'
										elif obj[12]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]>0:
									# {"feature": "Driving_to", "instances": 17, "metric_value": 0.874, "depth": 9}
									if obj[0]<=0:
										# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[6]>0:
											# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[12]<=9:
												return 'False'
											elif obj[12]>9:
												# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[8]<=2:
													# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[3]>55:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7]>0:
															return 'True'
														elif obj[7]<=0:
															return 'False'
														else: return 'False'
													elif obj[3]<=55:
														return 'False'
													else: return 'False'
												elif obj[8]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[14]<=-1.0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[9]>2:
						return 'True'
					else: return 'True'
				elif obj[15]>2.0:
					# {"feature": "Gender", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[7]<=0:
						return 'True'
					elif obj[7]>0:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2:
							return 'True'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[20]>2:
				# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[14]<=0.0:
				return 'False'
			elif obj[14]>0.0:
				# {"feature": "Weather", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[8]<=4:
						return 'False'
					elif obj[8]>4:
						return 'True'
					else: return 'True'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[13]>6:
		# {"feature": "Children", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[10]<=0:
			return 'True'
		elif obj[10]>0:
			# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
