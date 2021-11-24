def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[11]<=11:
		# {"feature": "Passanger", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[0]>0:
			# {"feature": "Coupon", "instances": 21, "metric_value": 0.7919, "depth": 3}
			if obj[4]>2:
				# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[12]<=5:
					# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3]>1:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=4:
								return 'False'
							elif obj[7]>4:
								return 'True'
							else: return 'True'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[12]>5:
					return 'False'
				else: return 'False'
			elif obj[4]<=2:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[11]>11:
		# {"feature": "Children", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[9]>0:
			return 'False'
		elif obj[9]<=0:
			# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]>2:
				return 'False'
			elif obj[4]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
