def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Age", "instances": 32, "metric_value": 0.9972, "depth": 2}
		if obj[8]>0:
			# {"feature": "Education", "instances": 28, "metric_value": 0.9666, "depth": 3}
			if obj[11]>1:
				# {"feature": "Temperature", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[3]>55:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[9]<=1:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=3:
								return 'False'
							elif obj[5]>3:
								return 'True'
							else: return 'True'
						elif obj[9]>1:
							return 'True'
						else: return 'True'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				elif obj[3]<=55:
					return 'False'
				else: return 'False'
			elif obj[11]<=1:
				# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[15]>1.0:
					# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[13]>1:
						return 'True'
					elif obj[13]<=1:
						return 'False'
					else: return 'False'
				elif obj[15]<=1.0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[12]>1:
						return 'False'
					elif obj[12]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=0:
			return 'True'
		else: return 'True'
	elif obj[1]>1:
		# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[9]<=1:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[5]>1:
				return 'True'
			elif obj[5]<=1:
				# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[14]<=1.0:
					return 'False'
				elif obj[14]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>1:
			# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[6]>0:
				return 'False'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
