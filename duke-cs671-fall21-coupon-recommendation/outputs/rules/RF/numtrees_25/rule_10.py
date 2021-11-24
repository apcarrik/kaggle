def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Occupation", "instances": 41, "metric_value": 0.9996, "depth": 1}
	if obj[12]>6:
		# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[18]<=1.0:
			# {"feature": "Time", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Temperature", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[3]>30:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[1]>0:
						# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]<=3:
								return 'False'
							elif obj[5]>3:
								# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=0:
									return 'True'
								elif obj[0]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=30:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[18]>1.0:
			return 'True'
		else: return 'True'
	elif obj[12]<=6:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[5]>1:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[4]>1:
				# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[7]>0:
					return 'False'
				elif obj[7]<=0:
					# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=0:
						return 'True'
					elif obj[0]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		elif obj[5]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
