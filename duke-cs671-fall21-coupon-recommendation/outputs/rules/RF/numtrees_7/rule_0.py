def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 146, "metric_value": 0.9651, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coffeehouse", "instances": 102, "metric_value": 0.886, "depth": 2}
		if obj[15]>0.0:
			# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.801, "depth": 3}
			if obj[18]>0.0:
				# {"feature": "Occupation", "instances": 66, "metric_value": 0.866, "depth": 4}
				if obj[12]<=7:
					# {"feature": "Age", "instances": 39, "metric_value": 0.679, "depth": 5}
					if obj[8]<=6:
						# {"feature": "Bar", "instances": 38, "metric_value": 0.6292, "depth": 6}
						if obj[14]>0.0:
							# {"feature": "Direction_same", "instances": 21, "metric_value": 0.7919, "depth": 7}
							if obj[19]<=0:
								# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.7219, "depth": 8}
								if obj[17]>2.0:
									# {"feature": "Driving_to", "instances": 12, "metric_value": 0.4138, "depth": 9}
									if obj[0]<=0:
										return 'True'
									elif obj[0]>0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[7]>0:
											# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										elif obj[7]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[17]<=2.0:
									# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[13]>2:
											# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[0]<=1:
												return 'False'
											elif obj[0]>1:
												return 'True'
											else: return 'True'
										elif obj[13]<=2:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[19]>0:
								return 'False'
							else: return 'False'
						elif obj[14]<=0.0:
							# {"feature": "Time", "instances": 17, "metric_value": 0.3228, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								# {"feature": "Driving_to", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[0]>0:
									return 'True'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[8]>6:
						return 'False'
					else: return 'False'
				elif obj[12]>7:
					# {"feature": "Weather", "instances": 27, "metric_value": 0.9911, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Age", "instances": 24, "metric_value": 0.9544, "depth": 6}
						if obj[8]<=4:
							# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Income", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[13]<=3:
									# {"feature": "Carryaway", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[16]<=3.0:
										return 'False'
									elif obj[16]>3.0:
										return 'True'
									else: return 'True'
								elif obj[13]>3:
									# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[17]<=2.0:
										return 'True'
									elif obj[17]>2.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[11]>2:
								# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[13]<=4:
									return 'True'
								elif obj[13]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>4:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[18]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[15]<=0.0:
			# {"feature": "Temperature", "instances": 24, "metric_value": 1.0, "depth": 3}
			if obj[3]>30:
				# {"feature": "Weather", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[19]<=0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[12]<=12:
							return 'False'
						elif obj[12]>12:
							return 'True'
						else: return 'True'
					elif obj[19]>0:
						# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			elif obj[3]<=30:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Weather", "instances": 44, "metric_value": 0.976, "depth": 2}
		if obj[2]<=0:
			# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.9994, "depth": 3}
			if obj[18]>0.0:
				# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 4}
				if obj[12]>1:
					# {"feature": "Bar", "instances": 26, "metric_value": 1.0, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Carryaway", "instances": 23, "metric_value": 0.9877, "depth": 6}
						if obj[16]>2.0:
							# {"feature": "Income", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[13]<=2:
								# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							elif obj[13]>2:
								return 'False'
							else: return 'False'
						elif obj[16]<=2.0:
							# {"feature": "Driving_to", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[0]<=0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>30:
										return 'True'
									elif obj[3]<=30:
										return 'False'
									else: return 'False'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							elif obj[0]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[14]>2.0:
						return 'True'
					else: return 'True'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			elif obj[18]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[2]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
