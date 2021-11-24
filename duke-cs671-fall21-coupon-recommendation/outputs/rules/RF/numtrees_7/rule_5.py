def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 146, "metric_value": 0.9988, "depth": 1}
	if obj[5]>1:
		# {"feature": "Restaurantlessthan20", "instances": 106, "metric_value": 0.9907, "depth": 2}
		if obj[17]<=2.0:
			# {"feature": "Driving_to", "instances": 66, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=0:
				# {"feature": "Occupation", "instances": 42, "metric_value": 0.7919, "depth": 4}
				if obj[12]>4:
					# {"feature": "Age", "instances": 29, "metric_value": 0.5788, "depth": 5}
					if obj[8]>0:
						# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.3912, "depth": 6}
						if obj[15]>0.0:
							return 'True'
						elif obj[15]<=0.0:
							# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[14]<=0.0:
									return 'True'
								elif obj[14]>0.0:
									return 'False'
								else: return 'False'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]<=0:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=4:
					# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[11]>0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[20]>1:
							# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[2]<=1:
								return 'False'
							elif obj[2]>1:
								return 'True'
							else: return 'True'
						elif obj[20]<=1:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=2:
								return 'True'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>0:
				# {"feature": "Bar", "instances": 24, "metric_value": 1.0, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[12]>2:
						# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[15]<=2.0:
							return 'False'
						elif obj[15]>2.0:
							return 'True'
						else: return 'True'
					elif obj[12]<=2:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=4:
							return 'True'
						elif obj[8]>4:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[14]>1.0:
					# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[8]>1:
						return 'True'
					elif obj[8]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[17]>2.0:
			# {"feature": "Children", "instances": 40, "metric_value": 0.9544, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Driving_to", "instances": 27, "metric_value": 0.999, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 6}
						if obj[20]>1:
							# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[6]>0:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[1]>1:
									# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=2:
										return 'True'
									elif obj[4]>2:
										return 'False'
									else: return 'False'
								elif obj[1]<=1:
									return 'False'
								else: return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[20]<=1:
							return 'True'
						else: return 'True'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[10]>0:
				# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Age", "instances": 40, "metric_value": 0.8485, "depth": 2}
		if obj[8]<=6:
			# {"feature": "Gender", "instances": 38, "metric_value": 0.7897, "depth": 3}
			if obj[7]>0:
				# {"feature": "Passanger", "instances": 23, "metric_value": 0.4262, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[14]<=1.0:
							return 'True'
						elif obj[14]>1.0:
							return 'False'
						else: return 'False'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]<=0:
				# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[14]<=0.0:
						# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>0:
							# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>55:
								return 'True'
							elif obj[3]<=55:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[14]>0.0:
						return 'True'
					else: return 'True'
				elif obj[6]>0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[11]<=2:
						return 'False'
					elif obj[11]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
