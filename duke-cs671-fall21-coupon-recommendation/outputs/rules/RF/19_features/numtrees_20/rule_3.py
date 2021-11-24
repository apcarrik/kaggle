def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[7]<=3:
		# {"feature": "Weather", "instances": 34, "metric_value": 0.9975, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[11]<=8:
						# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[12]>4:
							return 'True'
						elif obj[12]<=4:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]>8:
						return 'False'
					else: return 'False'
				elif obj[15]>2.0:
					return 'True'
				else: return 'True'
			elif obj[4]>3:
				# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[9]<=0:
							return 'True'
						elif obj[9]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	elif obj[7]>3:
		# {"feature": "Temperature", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[2]>30:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[13]<=2.0:
				return 'True'
			elif obj[13]>2.0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0:
					return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=30:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				return 'False'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
