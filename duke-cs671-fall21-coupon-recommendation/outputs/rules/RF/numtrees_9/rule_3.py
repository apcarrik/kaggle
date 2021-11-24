def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coffeehouse", "instances": 113, "metric_value": 0.9904, "depth": 1}
	if obj[15]>1.0:
		# {"feature": "Income", "instances": 59, "metric_value": 0.8874, "depth": 2}
		if obj[13]>2:
			# {"feature": "Coupon_validity", "instances": 39, "metric_value": 0.9766, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Weather", "instances": 21, "metric_value": 0.7025, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[18]<=3.0:
						return 'True'
					elif obj[18]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]>0:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=2:
						return 'False'
					elif obj[9]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>0:
				# {"feature": "Age", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[8]>1:
					# {"feature": "Gender", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[7]>0:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[18]>0.0:
							return 'False'
						elif obj[18]<=0.0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=3:
								return 'False'
							elif obj[5]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]<=2:
			# {"feature": "Direction_same", "instances": 20, "metric_value": 0.469, "depth": 3}
			if obj[19]<=0:
				return 'True'
			elif obj[19]>0:
				# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=0:
					return 'False'
				elif obj[6]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[15]<=1.0:
		# {"feature": "Time", "instances": 54, "metric_value": 0.9751, "depth": 2}
		if obj[4]>0:
			# {"feature": "Weather", "instances": 42, "metric_value": 0.8926, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Education", "instances": 33, "metric_value": 0.9673, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Restaurantlessthan20", "instances": 27, "metric_value": 0.999, "depth": 5}
					if obj[17]<=2.0:
						# {"feature": "Income", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[13]<=3:
							return 'False'
						elif obj[13]>3:
							# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=0:
									return 'False'
								elif obj[0]>0:
									return 'True'
								else: return 'True'
							elif obj[10]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[17]>2.0:
						# {"feature": "Children", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[8]>0:
								# {"feature": "Carryaway", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[16]<=2.0:
									return 'True'
								elif obj[16]>2.0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=1:
										return 'False'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]<=0:
								return 'False'
							else: return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[11]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[8]>1:
				# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				elif obj[7]>0:
					return 'False'
				else: return 'False'
			elif obj[8]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
