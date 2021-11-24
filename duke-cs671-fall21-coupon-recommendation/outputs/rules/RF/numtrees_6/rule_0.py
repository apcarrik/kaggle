def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 170, "metric_value": 0.9951, "depth": 1}
	if obj[5]>0:
		# {"feature": "Driving_to", "instances": 138, "metric_value": 0.9656, "depth": 2}
		if obj[0]<=0:
			# {"feature": "Education", "instances": 72, "metric_value": 0.8524, "depth": 3}
			if obj[11]<=3:
				# {"feature": "Occupation", "instances": 65, "metric_value": 0.8905, "depth": 4}
				if obj[12]<=9:
					# {"feature": "Coffeehouse", "instances": 47, "metric_value": 0.785, "depth": 5}
					if obj[15]<=3.0:
						# {"feature": "Gender", "instances": 42, "metric_value": 0.7025, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.8631, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Bar", "instances": 20, "metric_value": 0.8113, "depth": 8}
								if obj[14]<=1.0:
									# {"feature": "Weather", "instances": 14, "metric_value": 0.9403, "depth": 9}
									if obj[2]<=0:
										# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 10}
										if obj[8]>3:
											# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[4]>2:
												return 'True'
											elif obj[4]<=2:
												# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[6]>0:
														# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=0:
															return 'False'
														elif obj[13]>0:
															return 'True'
														else: return 'True'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]<=3:
											return 'False'
										else: return 'False'
									elif obj[2]>0:
										return 'True'
									else: return 'True'
								elif obj[14]>1.0:
									return 'True'
								else: return 'True'
							elif obj[9]>1:
								return 'False'
							else: return 'False'
						elif obj[7]>0:
							# {"feature": "Carryaway", "instances": 21, "metric_value": 0.4537, "depth": 7}
							if obj[16]>0.0:
								# {"feature": "Income", "instances": 20, "metric_value": 0.2864, "depth": 8}
								if obj[13]<=4:
									return 'True'
								elif obj[13]>4:
									# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[6]<=0:
										return 'True'
									elif obj[6]>0:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[4]>2:
											return 'True'
										elif obj[4]<=2:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[16]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[15]>3.0:
						# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]>55:
							return 'False'
						elif obj[3]<=55:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]>9:
					# {"feature": "Passanger", "instances": 18, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Gender", "instances": 16, "metric_value": 0.9887, "depth": 6}
						if obj[7]>0:
							# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[8]>1:
								# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[4]>2:
									# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[13]>0:
										return 'True'
									elif obj[13]<=0:
										return 'False'
									else: return 'False'
								elif obj[4]<=2:
									return 'False'
								else: return 'False'
							elif obj[8]<=1:
								return 'True'
							else: return 'True'
						elif obj[7]<=0:
							# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[9]>0:
								return 'False'
							elif obj[9]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[11]>3:
				return 'True'
			else: return 'True'
		elif obj[0]>0:
			# {"feature": "Direction_same", "instances": 66, "metric_value": 0.9993, "depth": 3}
			if obj[19]<=0:
				# {"feature": "Coupon_validity", "instances": 44, "metric_value": 0.9457, "depth": 4}
				if obj[6]>0:
					# {"feature": "Carryaway", "instances": 24, "metric_value": 0.65, "depth": 5}
					if obj[16]>1.0:
						# {"feature": "Income", "instances": 22, "metric_value": 0.4395, "depth": 6}
						if obj[13]<=4:
							return 'False'
						elif obj[13]>4:
							# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[9]>0:
								return 'False'
							elif obj[9]<=0:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=4:
									return 'True'
								elif obj[8]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[16]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[6]<=0:
					# {"feature": "Maritalstatus", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[9]>0:
						# {"feature": "Bar", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[14]>1.0:
							# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[2]<=0:
									return 'True'
								elif obj[2]>0:
									# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=30:
										return 'True'
									elif obj[3]>30:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[11]>2:
								return 'False'
							else: return 'False'
						elif obj[14]<=1.0:
							return 'True'
						else: return 'True'
					elif obj[9]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[19]>0:
				# {"feature": "Income", "instances": 22, "metric_value": 0.8454, "depth": 4}
				if obj[13]<=3:
					# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[9]>0:
						# {"feature": "Temperature", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[3]>30:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[15]<=2.0:
								return 'False'
							elif obj[15]>2.0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]<=30:
							return 'True'
						else: return 'True'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				elif obj[13]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]<=0:
		# {"feature": "Bar", "instances": 32, "metric_value": 0.8113, "depth": 2}
		if obj[14]<=0.0:
			# {"feature": "Time", "instances": 18, "metric_value": 0.3095, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[14]>0.0:
			# {"feature": "Age", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[8]>1:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[13]<=5:
						return 'False'
					elif obj[13]>5:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[8]<=1:
				# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]<=55:
					return 'True'
				elif obj[3]>55:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'
