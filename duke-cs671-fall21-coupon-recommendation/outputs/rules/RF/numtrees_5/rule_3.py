def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon_validity", "instances": 204, "metric_value": 0.9748, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Age", "instances": 109, "metric_value": 0.8954, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Coupon", "instances": 63, "metric_value": 0.9779, "depth": 3}
			if obj[5]>1:
				# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.9103, "depth": 4}
				if obj[18]<=3.0:
					# {"feature": "Income", "instances": 41, "metric_value": 0.8722, "depth": 5}
					if obj[13]<=6:
						# {"feature": "Restaurantlessthan20", "instances": 36, "metric_value": 0.9183, "depth": 6}
						if obj[17]>1.0:
							# {"feature": "Time", "instances": 30, "metric_value": 0.7838, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Temperature", "instances": 24, "metric_value": 0.8709, "depth": 8}
								if obj[3]>30:
									# {"feature": "Occupation", "instances": 18, "metric_value": 0.65, "depth": 9}
									if obj[12]<=11:
										# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.3534, "depth": 10}
										if obj[15]<=3.0:
											return 'True'
										elif obj[15]>3.0:
											return 'False'
										else: return 'False'
									elif obj[12]>11:
										# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]>0:
											return 'False'
										elif obj[9]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]<=30:
									# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[0]>0:
										return 'False'
									elif obj[0]<=0:
										# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2]>0:
											return 'True'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[17]<=1.0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[4]>1:
								return 'False'
							elif obj[4]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>6:
						return 'True'
					else: return 'True'
				elif obj[18]>3.0:
					return 'False'
				else: return 'False'
			elif obj[5]<=1:
				# {"feature": "Gender", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[14]>1.0:
						# {"feature": "Driving_to", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[15]<=3.0:
								return 'True'
							elif obj[15]>3.0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[14]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[7]>0:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[14]<=1.0:
						return 'False'
					elif obj[14]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>2:
			# {"feature": "Income", "instances": 46, "metric_value": 0.6666, "depth": 3}
			if obj[13]>3:
				# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Carryaway", "instances": 18, "metric_value": 0.9911, "depth": 5}
					if obj[16]>2.0:
						# {"feature": "Driving_to", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[17]<=2.0:
								return 'False'
							elif obj[17]>2.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[16]<=2.0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>0:
								return 'False'
							elif obj[7]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[13]<=3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[6]>0:
		# {"feature": "Passanger", "instances": 95, "metric_value": 0.9993, "depth": 2}
		if obj[1]>0:
			# {"feature": "Driving_to", "instances": 86, "metric_value": 0.9965, "depth": 3}
			if obj[0]>0:
				# {"feature": "Gender", "instances": 45, "metric_value": 0.9825, "depth": 4}
				if obj[7]>0:
					# {"feature": "Carryaway", "instances": 28, "metric_value": 0.8113, "depth": 5}
					if obj[16]<=2.0:
						# {"feature": "Weather", "instances": 18, "metric_value": 0.3095, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[8]>0:
								return 'False'
							elif obj[8]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[16]>2.0:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[12]>5:
							return 'True'
						elif obj[12]<=5:
							# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]>30:
								return 'False'
							elif obj[3]<=30:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[7]<=0:
					# {"feature": "Temperature", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[3]<=55:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[11]<=1:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[8]>0:
								return 'True'
							elif obj[8]<=0:
								return 'False'
							else: return 'False'
						elif obj[11]>1:
							return 'False'
						else: return 'False'
					elif obj[3]>55:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Time", "instances": 41, "metric_value": 0.9262, "depth": 4}
				if obj[4]>2:
					# {"feature": "Income", "instances": 27, "metric_value": 0.9911, "depth": 5}
					if obj[13]<=6:
						# {"feature": "Occupation", "instances": 25, "metric_value": 0.971, "depth": 6}
						if obj[12]<=6:
							# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[17]>2.0:
										return 'True'
									elif obj[17]<=2.0:
										# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]>30:
											return 'False'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[11]>2:
									return 'False'
								else: return 'False'
							elif obj[5]>2:
								return 'True'
							else: return 'True'
						elif obj[12]>6:
							# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[17]>1.0:
								# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[9]<=1:
									return 'False'
								elif obj[9]>1:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[17]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>6:
						return 'False'
					else: return 'False'
				elif obj[4]<=2:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[12]>2:
						return 'True'
					elif obj[12]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
