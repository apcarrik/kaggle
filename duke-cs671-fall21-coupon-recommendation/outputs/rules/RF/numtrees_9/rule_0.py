def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon_validity", "instances": 113, "metric_value": 0.9999, "depth": 1}
	if obj[6]>0:
		# {"feature": "Coupon", "instances": 60, "metric_value": 0.9604, "depth": 2}
		if obj[5]>1:
			# {"feature": "Passanger", "instances": 54, "metric_value": 0.9841, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Carryaway", "instances": 33, "metric_value": 0.885, "depth": 4}
				if obj[16]>1.0:
					# {"feature": "Maritalstatus", "instances": 28, "metric_value": 0.9403, "depth": 5}
					if obj[9]>0:
						# {"feature": "Age", "instances": 18, "metric_value": 0.7642, "depth": 6}
						if obj[8]>2:
							# {"feature": "Weather", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[3]>30:
									# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[12]>2:
										return 'False'
									elif obj[12]<=2:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[11]<=0:
											return 'False'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]<=30:
									return 'True'
								else: return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						elif obj[8]<=2:
							return 'False'
						else: return 'False'
					elif obj[9]<=0:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[12]>5:
							# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=55:
									return 'False'
								elif obj[3]>55:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]<=5:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]<=3:
								return 'False'
							elif obj[8]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[16]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Income", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[13]<=4:
					# {"feature": "Gender", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[7]>0:
						# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[12]<=14:
							# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[15]>0.0:
								return 'True'
							elif obj[15]<=0.0:
								# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[16]>1.0:
									return 'False'
								elif obj[16]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]>14:
							return 'False'
						else: return 'False'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				elif obj[13]>4:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]<=1:
			return 'False'
		else: return 'False'
	elif obj[6]<=0:
		# {"feature": "Coupon", "instances": 53, "metric_value": 0.9414, "depth": 2}
		if obj[5]>0:
			# {"feature": "Weather", "instances": 41, "metric_value": 0.8015, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.5788, "depth": 4}
				if obj[18]<=1.0:
					# {"feature": "Income", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[13]>3:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[12]>6:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[14]<=0.0:
								return 'True'
							elif obj[14]>0.0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=3:
									return 'False'
								elif obj[11]>3:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]<=6:
							return 'False'
						else: return 'False'
					elif obj[13]<=3:
						return 'True'
					else: return 'True'
				elif obj[18]>1.0:
					return 'True'
				else: return 'True'
			elif obj[2]>0:
				# {"feature": "Direction_same", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[19]<=0:
					# {"feature": "Driving_to", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=30:
							return 'True'
						elif obj[3]>30:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[19]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[18]<=2.0:
				# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			elif obj[18]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
