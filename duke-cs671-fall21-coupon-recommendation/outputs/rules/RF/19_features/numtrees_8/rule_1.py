def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Time", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[3]<=1:
		# {"feature": "Coupon", "instances": 76, "metric_value": 0.9875, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Occupation", "instances": 52, "metric_value": 0.9957, "depth": 3}
			if obj[11]>1:
				# {"feature": "Age", "instances": 45, "metric_value": 0.9968, "depth": 4}
				if obj[7]>0:
					# {"feature": "Income", "instances": 38, "metric_value": 0.9678, "depth": 5}
					if obj[12]<=4:
						# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.8404, "depth": 6}
						if obj[16]<=3.0:
							# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.7383, "depth": 7}
							if obj[15]<=2.0:
								# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 8}
								if obj[14]>0.0:
									# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[8]>0:
										# {"feature": "Temperature", "instances": 10, "metric_value": 1.0, "depth": 10}
										if obj[2]>30:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[18]<=2:
												# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[9]>0:
													return 'False'
												elif obj[9]<=0:
													# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1]<=0:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[6]<=0:
															return 'True'
														elif obj[6]>0:
															return 'False'
														else: return 'False'
													elif obj[1]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[18]>2:
												return 'True'
											else: return 'True'
										elif obj[2]<=30:
											return 'True'
										else: return 'True'
									elif obj[8]<=0:
										return 'False'
									else: return 'False'
								elif obj[14]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[15]>2.0:
								return 'False'
							else: return 'False'
						elif obj[16]>3.0:
							return 'True'
						else: return 'True'
					elif obj[12]>4:
						# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[10]<=2:
							# {"feature": "Temperature", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[2]<=55:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[14]<=2.0:
									return 'True'
								elif obj[14]>2.0:
									# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'False'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[2]>55:
								return 'False'
							else: return 'False'
						elif obj[10]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[7]<=0:
					# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[12]<=4:
						return 'True'
					elif obj[12]>4:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]<=1:
				return 'True'
			else: return 'True'
		elif obj[4]>3:
			# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.7383, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.4855, "depth": 4}
				if obj[8]<=1:
					return 'False'
				elif obj[8]>1:
					# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[12]<=4:
						return 'False'
					elif obj[12]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[14]>2.0:
				# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=55:
					return 'True'
				elif obj[2]>55:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[3]>1:
		# {"feature": "Occupation", "instances": 51, "metric_value": 0.8974, "depth": 2}
		if obj[11]<=11:
			# {"feature": "Coupon", "instances": 41, "metric_value": 0.7593, "depth": 3}
			if obj[4]>1:
				# {"feature": "Coupon_validity", "instances": 32, "metric_value": 0.5436, "depth": 4}
				if obj[5]>0:
					# {"feature": "Age", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[7]>2:
						# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[12]<=4:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[10]>0:
								# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[15]>1.0:
									return 'False'
								elif obj[15]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[10]<=0:
								return 'True'
							else: return 'True'
						elif obj[12]>4:
							return 'True'
						else: return 'True'
					elif obj[7]<=2:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[7]<=4:
					# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[2]<=55:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[10]<=2:
							return 'False'
						elif obj[10]>2:
							return 'True'
						else: return 'True'
					elif obj[2]>55:
						return 'True'
					else: return 'True'
				elif obj[7]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]>11:
			# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[8]<=1:
				# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[12]<=4:
					return 'True'
				elif obj[12]>4:
					return 'False'
				else: return 'False'
			elif obj[8]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
