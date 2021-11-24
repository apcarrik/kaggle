def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Coffeehouse", "instances": 84, "metric_value": 1.0, "depth": 2}
		if obj[15]<=2.0:
			# {"feature": "Age", "instances": 68, "metric_value": 0.9843, "depth": 3}
			if obj[8]>0:
				# {"feature": "Maritalstatus", "instances": 56, "metric_value": 0.9241, "depth": 4}
				if obj[9]>0:
					# {"feature": "Time", "instances": 40, "metric_value": 0.9928, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Occupation", "instances": 27, "metric_value": 0.9751, "depth": 6}
						if obj[12]>1:
							# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 7}
							if obj[5]>1:
								# {"feature": "Coupon_validity", "instances": 19, "metric_value": 0.9495, "depth": 8}
								if obj[6]>0:
									# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[18]<=1.0:
										# {"feature": "Driving_to", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[3]>30:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7]>0:
													# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[7]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[18]>1.0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=1:
								return 'False'
							else: return 'False'
						elif obj[12]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>2:
						# {"feature": "Temperature", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[3]>55:
							return 'False'
						elif obj[3]<=55:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[11]>0:
								return 'False'
							elif obj[11]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[9]<=0:
					# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.3373, "depth": 5}
					if obj[17]>1.0:
						return 'False'
					elif obj[17]<=1.0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[8]<=0:
				# {"feature": "Temperature", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[3]>30:
					# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[17]>-1.0:
						return 'True'
					elif obj[17]<=-1.0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=30:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]>2.0:
			# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[17]<=3.0:
				# {"feature": "Weather", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			elif obj[17]>3.0:
				# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[1]>1:
		# {"feature": "Carryaway", "instances": 43, "metric_value": 0.8204, "depth": 2}
		if obj[16]>0.0:
			# {"feature": "Temperature", "instances": 40, "metric_value": 0.7219, "depth": 3}
			if obj[3]>55:
				# {"feature": "Age", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=4:
					# {"feature": "Income", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[13]<=7:
						# {"feature": "Bar", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[14]<=0.0:
							# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]<=2:
										return 'True'
									elif obj[11]>2:
										return 'False'
									else: return 'False'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						elif obj[14]>0.0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]<=2:
								return 'False'
							elif obj[4]>2:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[11]<=0:
									return 'True'
								elif obj[11]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[13]>7:
						return 'True'
					else: return 'True'
				elif obj[8]>4:
					return 'True'
				else: return 'True'
			elif obj[3]<=55:
				# {"feature": "Driving_to", "instances": 19, "metric_value": 0.2975, "depth": 4}
				if obj[0]<=0:
					return 'True'
				elif obj[0]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[16]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'True'
