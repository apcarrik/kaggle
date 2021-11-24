def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coffeehouse", "instances": 146, "metric_value": 0.9988, "depth": 1}
	if obj[15]<=1.0:
		# {"feature": "Occupation", "instances": 77, "metric_value": 0.9457, "depth": 2}
		if obj[12]>3:
			# {"feature": "Coupon", "instances": 56, "metric_value": 0.8631, "depth": 3}
			if obj[5]>1:
				# {"feature": "Passanger", "instances": 43, "metric_value": 0.933, "depth": 4}
				if obj[1]>0:
					# {"feature": "Temperature", "instances": 38, "metric_value": 0.868, "depth": 5}
					if obj[3]>30:
						# {"feature": "Age", "instances": 29, "metric_value": 0.7355, "depth": 6}
						if obj[8]>1:
							# {"feature": "Children", "instances": 21, "metric_value": 0.8631, "depth": 7}
							if obj[10]>0:
								# {"feature": "Carryaway", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[16]<=3.0:
									# {"feature": "Income", "instances": 10, "metric_value": 1.0, "depth": 9}
									if obj[13]>4:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[14]<=0.0:
											# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[0]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[19]<=0:
													return 'False'
												elif obj[19]>0:
													return 'True'
												else: return 'True'
											elif obj[0]<=0:
												return 'True'
											else: return 'True'
										elif obj[14]>0.0:
											return 'False'
										else: return 'False'
									elif obj[13]<=4:
										return 'True'
									else: return 'True'
								elif obj[16]>3.0:
									return 'False'
								else: return 'False'
							elif obj[10]<=0:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[14]<=1.0:
									return 'False'
								elif obj[14]>1.0:
									# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]<=30:
						# {"feature": "Carryaway", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[16]>1.0:
							# {"feature": "Driving_to", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>0:
									return 'False'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[16]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=1:
				# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[11]<=3:
					return 'False'
				elif obj[11]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]<=3:
			# {"feature": "Income", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[13]>0:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[18]<=1.0:
					# {"feature": "Driving_to", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[0]<=0:
						# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[8]<=2:
							return 'True'
						elif obj[8]>2:
							# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]>0:
						return 'False'
					else: return 'False'
				elif obj[18]>1.0:
					return 'True'
				else: return 'True'
			elif obj[13]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[15]>1.0:
		# {"feature": "Carryaway", "instances": 69, "metric_value": 0.8865, "depth": 2}
		if obj[16]>1.0:
			# {"feature": "Passanger", "instances": 60, "metric_value": 0.7838, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Coupon", "instances": 40, "metric_value": 0.9341, "depth": 4}
				if obj[5]>1:
					# {"feature": "Maritalstatus", "instances": 24, "metric_value": 0.7383, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.4855, "depth": 6}
						if obj[12]>5:
							return 'True'
						elif obj[12]<=5:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[4]>1:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2]<=0:
										return 'False'
									elif obj[2]>0:
										return 'True'
									else: return 'True'
								elif obj[11]>2:
									return 'True'
								else: return 'True'
							elif obj[4]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[9]>1:
						# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=0:
							# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=0:
								return 'True'
							elif obj[10]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]<=1:
					# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[12]<=10:
						# {"feature": "Income", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[13]<=4:
							return 'False'
						elif obj[13]>4:
							# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]>10:
						# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[8]>0:
							return 'True'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[16]<=1.0:
			# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[19]<=0:
				# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[13]>2:
					return 'False'
				elif obj[13]<=2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>2:
						return 'False'
					elif obj[1]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[19]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
