def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[17]<=1.0:
		# {"feature": "Time", "instances": 54, "metric_value": 0.996, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Age", "instances": 44, "metric_value": 0.9624, "depth": 3}
			if obj[8]>0:
				# {"feature": "Coupon_validity", "instances": 38, "metric_value": 0.992, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[12]<=6:
							# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[13]>2:
								return 'True'
							elif obj[13]<=2:
								return 'False'
							else: return 'False'
						elif obj[12]>6:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[6]>0:
					# {"feature": "Temperature", "instances": 19, "metric_value": 0.8315, "depth": 5}
					if obj[3]>55:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[19]>1:
							# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[11]<=3:
									return 'True'
								elif obj[11]>3:
									return 'False'
								else: return 'False'
							elif obj[9]>1:
								return 'False'
							else: return 'False'
						elif obj[19]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]<=55:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[8]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]>3:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[5]>3:
				return 'True'
			elif obj[5]<=3:
				# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[14]<=0.0:
					return 'False'
				elif obj[14]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[17]>1.0:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.8238, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Age", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[8]<=6:
				return 'True'
			elif obj[8]>6:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>2:
			# {"feature": "Gender", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Weather", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[2]<=0:
					return 'True'
				elif obj[2]>0:
					# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
