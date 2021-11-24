def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 146, "metric_value": 0.9733, "depth": 1}
	if obj[5]>0:
		# {"feature": "Coupon_validity", "instances": 125, "metric_value": 0.9209, "depth": 2}
		if obj[6]>0:
			# {"feature": "Driving_to", "instances": 70, "metric_value": 0.9906, "depth": 3}
			if obj[0]<=0:
				# {"feature": "Weather", "instances": 36, "metric_value": 0.888, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Income", "instances": 34, "metric_value": 0.8338, "depth": 5}
					if obj[13]<=5:
						# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.9427, "depth": 6}
						if obj[15]>1.0:
							# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[17]<=3.0:
								return 'True'
							elif obj[17]>3.0:
								# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[8]<=3:
									return 'False'
								elif obj[8]>3:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[15]<=1.0:
							# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[1]>0:
								# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[20]<=1:
									return 'False'
								elif obj[20]>1:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>1:
										return 'True'
									elif obj[8]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>5:
						return 'True'
					else: return 'True'
				elif obj[2]>0:
					return 'False'
				else: return 'False'
			elif obj[0]>0:
				# {"feature": "Restaurantlessthan20", "instances": 34, "metric_value": 0.9774, "depth": 4}
				if obj[17]<=2.0:
					# {"feature": "Temperature", "instances": 24, "metric_value": 0.995, "depth": 5}
					if obj[3]>30:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 6}
						if obj[12]<=7:
							# {"feature": "Maritalstatus", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[15]<=1.0:
									return 'False'
								elif obj[15]>1.0:
									# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[8]<=4:
										return 'True'
									elif obj[8]>4:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[9]>1:
								return 'True'
							else: return 'True'
						elif obj[12]>7:
							return 'False'
						else: return 'False'
					elif obj[3]<=30:
						return 'True'
					else: return 'True'
				elif obj[17]>2.0:
					# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[13]>0:
						return 'False'
					elif obj[13]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[6]<=0:
			# {"feature": "Restaurantlessthan20", "instances": 55, "metric_value": 0.7219, "depth": 3}
			if obj[17]>1.0:
				# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.8113, "depth": 4}
				if obj[15]<=1.0:
					# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8315, "depth": 6}
						if obj[18]>0.0:
							# {"feature": "Temperature", "instances": 17, "metric_value": 0.6723, "depth": 7}
							if obj[3]>30:
								return 'True'
							elif obj[3]<=30:
								# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[2]<=0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4]<=3:
										return 'False'
									elif obj[4]>3:
										return 'True'
									else: return 'True'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[18]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				elif obj[15]>1.0:
					# {"feature": "Occupation", "instances": 21, "metric_value": 0.4537, "depth": 5}
					if obj[12]<=14:
						# {"feature": "Passanger", "instances": 20, "metric_value": 0.2864, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]>14:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[17]<=1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Gender", "instances": 21, "metric_value": 0.7025, "depth": 2}
		if obj[7]>0:
			return 'False'
		elif obj[7]<=0:
			# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[3]>30:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]>3:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=1:
						return 'False'
					elif obj[9]>1:
						return 'True'
					else: return 'True'
				elif obj[4]<=3:
					return 'True'
				else: return 'True'
			elif obj[3]<=30:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
