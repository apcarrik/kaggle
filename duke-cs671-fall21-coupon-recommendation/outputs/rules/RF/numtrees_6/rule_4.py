def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 170, "metric_value": 0.9856, "depth": 1}
	if obj[5]>1:
		# {"feature": "Occupation", "instances": 127, "metric_value": 0.9379, "depth": 2}
		if obj[12]<=9:
			# {"feature": "Age", "instances": 96, "metric_value": 0.8571, "depth": 3}
			if obj[8]>0:
				# {"feature": "Coupon_validity", "instances": 79, "metric_value": 0.7513, "depth": 4}
				if obj[6]>0:
					# {"feature": "Passanger", "instances": 43, "metric_value": 0.9103, "depth": 5}
					if obj[1]>0:
						# {"feature": "Bar", "instances": 41, "metric_value": 0.8722, "depth": 6}
						if obj[14]<=1.0:
							# {"feature": "Time", "instances": 33, "metric_value": 0.7455, "depth": 7}
							if obj[4]>1:
								# {"feature": "Income", "instances": 17, "metric_value": 0.9774, "depth": 8}
								if obj[13]>2:
									# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[3]>55:
										# {"feature": "Children", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[10]<=0:
											return 'True'
										elif obj[10]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]>0:
												return 'True'
											elif obj[7]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[3]<=55:
										return 'False'
									else: return 'False'
								elif obj[13]<=2:
									# {"feature": "Driving_to", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[0]<=0:
										# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[3]>30:
											# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									elif obj[0]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]<=1:
								return 'True'
							else: return 'True'
						elif obj[14]>1.0:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[18]>0.0:
								# {"feature": "Driving_to", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=55:
										return 'False'
									elif obj[3]>55:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[18]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[6]<=0:
					# {"feature": "Passanger", "instances": 36, "metric_value": 0.4138, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						# {"feature": "Temperature", "instances": 16, "metric_value": 0.6962, "depth": 6}
						if obj[3]<=55:
							return 'True'
						elif obj[3]>55:
							# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[11]<=1:
									# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[13]>2:
										return 'True'
									elif obj[13]<=2:
										return 'False'
									else: return 'False'
								elif obj[11]>1:
									return 'False'
								else: return 'False'
							elif obj[9]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[8]<=0:
				# {"feature": "Weather", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[17]>0.0:
						# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[11]<=3:
								return 'False'
							elif obj[11]>3:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[17]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]>9:
			# {"feature": "Weather", "instances": 31, "metric_value": 0.9812, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Children", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Driving_to", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[0]>1:
									# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[3]>55:
										return 'False'
									elif obj[3]<=55:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							elif obj[9]>1:
								return 'False'
							else: return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[4]>3:
						return 'False'
					else: return 'False'
				elif obj[15]>2.0:
					return 'True'
				else: return 'True'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Age", "instances": 43, "metric_value": 0.933, "depth": 2}
		if obj[8]>1:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.7642, "depth": 3}
			if obj[12]<=8:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[20]<=2:
					# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[13]<=6:
						# {"feature": "Children", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>2:
									return 'False'
								elif obj[4]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[10]>0:
							# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[11]>0:
								return 'False'
							elif obj[11]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>6:
						return 'False'
					else: return 'False'
				elif obj[20]>2:
					return 'False'
				else: return 'False'
			elif obj[12]>8:
				return 'False'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Driving_to", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[6]<=0:
					return 'True'
				elif obj[6]>0:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[12]>1:
					return 'False'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
