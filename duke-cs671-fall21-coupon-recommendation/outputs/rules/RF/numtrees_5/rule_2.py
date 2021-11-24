def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9822, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coffeehouse", "instances": 148, "metric_value": 0.9291, "depth": 2}
		if obj[15]>1.0:
			# {"feature": "Education", "instances": 74, "metric_value": 0.7273, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Time", "instances": 59, "metric_value": 0.5726, "depth": 4}
				if obj[4]>0:
					# {"feature": "Carryaway", "instances": 43, "metric_value": 0.6931, "depth": 5}
					if obj[16]<=3.0:
						# {"feature": "Children", "instances": 38, "metric_value": 0.5618, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Maritalstatus", "instances": 25, "metric_value": 0.7219, "depth": 7}
							if obj[9]>0:
								# {"feature": "Income", "instances": 20, "metric_value": 0.469, "depth": 8}
								if obj[13]>3:
									return 'True'
								elif obj[13]<=3:
									# {"feature": "Driving_to", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=0:
										# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[3]>55:
											return 'False'
										elif obj[3]<=55:
											return 'True'
										else: return 'True'
									elif obj[0]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]<=0:
								# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=2:
										return 'True'
									elif obj[8]>2:
										return 'False'
									else: return 'False'
								elif obj[13]>4:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[16]>3.0:
						# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[11]>2:
				# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[6]>0:
					# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[8]<=3:
						return 'False'
					elif obj[8]>3:
						return 'True'
					else: return 'True'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[15]<=1.0:
			# {"feature": "Occupation", "instances": 74, "metric_value": 0.9995, "depth": 3}
			if obj[12]>2:
				# {"feature": "Passanger", "instances": 63, "metric_value": 0.9911, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Restaurantlessthan20", "instances": 48, "metric_value": 0.9377, "depth": 5}
					if obj[17]<=2.0:
						# {"feature": "Coupon_validity", "instances": 40, "metric_value": 0.9837, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Time", "instances": 21, "metric_value": 0.9852, "depth": 7}
							if obj[4]>0:
								# {"feature": "Education", "instances": 18, "metric_value": 1.0, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9887, "depth": 9}
									if obj[18]<=1.0:
										# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 10}
										if obj[14]<=2.0:
											# {"feature": "Income", "instances": 13, "metric_value": 0.8905, "depth": 11}
											if obj[13]<=4:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[19]<=0:
													# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[8]>0:
														return 'False'
													elif obj[8]<=0:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2]>0:
															return 'True'
														elif obj[2]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[19]>0:
													# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[9]<=0:
														return 'True'
													elif obj[9]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[13]>4:
												return 'False'
											else: return 'False'
										elif obj[14]>2.0:
											return 'True'
										else: return 'True'
									elif obj[18]>1.0:
										return 'True'
									else: return 'True'
								elif obj[11]>2:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Income", "instances": 19, "metric_value": 0.8315, "depth": 7}
							if obj[13]>0:
								# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.6723, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Bar", "instances": 16, "metric_value": 0.5436, "depth": 9}
									if obj[14]<=1.0:
										return 'False'
									elif obj[14]>1.0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[11]>0:
											# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[2]<=0:
													return 'True'
												elif obj[2]>0:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'True'
											else: return 'True'
										elif obj[11]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>2:
									return 'True'
								else: return 'True'
							elif obj[13]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[17]>2.0:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					# {"feature": "Age", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[8]>3:
						# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[17]>2.0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[17]<=2.0:
								return 'False'
							else: return 'False'
						elif obj[4]>2:
							return 'True'
						else: return 'True'
					elif obj[8]<=3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]<=2:
				# {"feature": "Carryaway", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[16]<=3.0:
					return 'True'
				elif obj[16]>3.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Bar", "instances": 56, "metric_value": 0.9544, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.9972, "depth": 3}
			if obj[18]<=2.0:
				# {"feature": "Income", "instances": 28, "metric_value": 0.9963, "depth": 4}
				if obj[13]>0:
					# {"feature": "Restaurantlessthan20", "instances": 26, "metric_value": 0.9829, "depth": 5}
					if obj[17]<=3.0:
						# {"feature": "Driving_to", "instances": 22, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[2]<=0:
										return 'False'
									elif obj[2]>0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]>1:
											return 'True'
										elif obj[8]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>3:
									return 'True'
								else: return 'True'
							elif obj[11]>2:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[12]<=7:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>2:
										return 'True'
									elif obj[8]<=2:
										return 'False'
									else: return 'False'
								elif obj[4]>0:
									return 'False'
								else: return 'False'
							elif obj[12]>7:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[17]>3.0:
						return 'False'
					else: return 'False'
				elif obj[13]<=0:
					return 'True'
				else: return 'True'
			elif obj[18]>2.0:
				return 'True'
			else: return 'True'
		elif obj[14]<=0.0:
			# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.65, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Education", "instances": 18, "metric_value": 0.3095, "depth": 4}
				if obj[11]<=3:
					return 'False'
				elif obj[11]>3:
					# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=0:
						return 'False'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]<=0.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=3:
						return 'False'
					elif obj[4]>3:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
