def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[9]>0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[12]<=7:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[16]<=2.0:
					# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[4]>0:
						return 'True'
					elif obj[4]<=0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>2:
							return 'False'
						elif obj[5]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[16]>2.0:
					return 'False'
				else: return 'False'
			elif obj[14]>2.0:
				return 'True'
			else: return 'True'
		elif obj[12]>7:
			return 'True'
		else: return 'True'
	elif obj[9]<=0:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[15]<=1.0:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[5]>0:
				# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[8]<=4:
					return 'True'
				elif obj[8]>4:
					return 'False'
				else: return 'False'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[15]>1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
