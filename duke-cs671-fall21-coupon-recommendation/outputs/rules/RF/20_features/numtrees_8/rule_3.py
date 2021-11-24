def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coffeehouse", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[15]<=1.0:
		# {"feature": "Age", "instances": 64, "metric_value": 0.9823, "depth": 2}
		if obj[8]>1:
			# {"feature": "Restaurantlessthan20", "instances": 39, "metric_value": 0.7793, "depth": 3}
			if obj[16]<=2.0:
				# {"feature": "Coupon", "instances": 27, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0:
					# {"feature": "Coupon_validity", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[6]>0:
						# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[17]<=1.0:
									# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[2]<=0:
										return 'False'
									elif obj[2]>0:
										# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=0:
											return 'True'
										elif obj[0]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[17]>1.0:
									return 'True'
								else: return 'True'
							elif obj[11]>0:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]<=0:
						# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[9]>0:
							return 'True'
						elif obj[9]<=0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[12]>4:
								return 'False'
							elif obj[12]<=4:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[16]>2.0:
				return 'False'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Passanger", "instances": 25, "metric_value": 0.8555, "depth": 3}
			if obj[1]>0:
				# {"feature": "Temperature", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[3]>30:
					# {"feature": "Bar", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[14]<=0.0:
						# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[14]>0.0:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=30:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[5]<=3:
						return 'True'
					elif obj[5]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[15]>1.0:
		# {"feature": "Temperature", "instances": 63, "metric_value": 0.9334, "depth": 2}
		if obj[3]<=55:
			# {"feature": "Age", "instances": 35, "metric_value": 0.9994, "depth": 3}
			if obj[8]>0:
				# {"feature": "Bar", "instances": 31, "metric_value": 0.9812, "depth": 4}
				if obj[14]<=0.0:
					# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[5]<=3:
						# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[16]<=2.0:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[19]>2:
								# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[19]<=2:
								return 'True'
							else: return 'True'
						elif obj[16]>2.0:
							return 'False'
						else: return 'False'
					elif obj[5]>3:
						return 'False'
					else: return 'False'
				elif obj[14]>0.0:
					# {"feature": "Time", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[12]<=14:
								# {"feature": "Driving_to", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]<=1:
										return 'False'
									elif obj[5]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[12]>14:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[8]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>55:
			# {"feature": "Bar", "instances": 28, "metric_value": 0.6769, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Education", "instances": 23, "metric_value": 0.4262, "depth": 4}
				if obj[11]<=2:
					return 'True'
				elif obj[11]>2:
					# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>2:
							return 'False'
						elif obj[8]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[14]>2.0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[5]>2:
					return 'False'
				elif obj[5]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
