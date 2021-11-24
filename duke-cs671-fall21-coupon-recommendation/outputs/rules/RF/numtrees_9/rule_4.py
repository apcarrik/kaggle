def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Maritalstatus", "instances": 113, "metric_value": 0.9699, "depth": 1}
	if obj[9]<=1:
		# {"feature": "Education", "instances": 82, "metric_value": 0.9142, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Coupon", "instances": 67, "metric_value": 0.8395, "depth": 3}
			if obj[5]>1:
				# {"feature": "Coupon_validity", "instances": 52, "metric_value": 0.7063, "depth": 4}
				if obj[6]>0:
					# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.8767, "depth": 5}
					if obj[15]<=2.0:
						# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 6}
						if obj[12]>1:
							# {"feature": "Driving_to", "instances": 18, "metric_value": 0.9911, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Passanger", "instances": 16, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 9}
									if obj[8]>2:
										# {"feature": "Children", "instances": 11, "metric_value": 0.994, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[3]>30:
												# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[2]<=0:
														# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]>1:
															return 'True'
														elif obj[13]<=1:
															return 'False'
														else: return 'False'
													elif obj[2]>0:
														return 'False'
													else: return 'False'
												elif obj[4]>1:
													return 'False'
												else: return 'False'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									elif obj[8]<=2:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[12]<=1:
							return 'True'
						else: return 'True'
					elif obj[15]>2.0:
						return 'True'
					else: return 'True'
				elif obj[6]<=0:
					# {"feature": "Carryaway", "instances": 25, "metric_value": 0.4022, "depth": 5}
					if obj[16]>-1.0:
						# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.2499, "depth": 6}
						if obj[15]<=2.0:
							return 'True'
						elif obj[15]>2.0:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[14]<=1.0:
								return 'True'
							elif obj[14]>1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[16]<=-1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=1:
				# {"feature": "Bar", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[14]<=0.0:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[12]<=5:
						return 'False'
					elif obj[12]>5:
						return 'True'
					else: return 'True'
				elif obj[14]>0.0:
					# {"feature": "Driving_to", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[13]<=1:
							return 'True'
						elif obj[13]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]>2:
			# {"feature": "Carryaway", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[16]>1.0:
				# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[13]<=6:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[20]>1:
							# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[20]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[13]>6:
					return 'True'
				else: return 'True'
			elif obj[16]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[9]>1:
		# {"feature": "Income", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[13]>2:
			# {"feature": "Time", "instances": 26, "metric_value": 1.0, "depth": 3}
			if obj[4]>2:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[12]<=17:
					# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[8]>0:
						return 'False'
					elif obj[8]<=0:
						# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[10]>0:
							return 'False'
						elif obj[10]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]>17:
					return 'True'
				else: return 'True'
			elif obj[4]<=2:
				# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=5:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[12]<=11:
						return 'True'
					elif obj[12]>11:
						return 'False'
					else: return 'False'
				elif obj[8]>5:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[13]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
