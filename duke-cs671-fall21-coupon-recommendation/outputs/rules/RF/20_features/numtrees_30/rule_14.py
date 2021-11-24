def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]>1:
		# {"feature": "Restaurantlessthan20", "instances": 25, "metric_value": 0.8555, "depth": 2}
		if obj[16]<=3.0:
			# {"feature": "Temperature", "instances": 22, "metric_value": 0.684, "depth": 3}
			if obj[3]>55:
				# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[9]>0:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[15]>0.0:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[18]<=0:
							return 'False'
						elif obj[18]>0:
							return 'True'
						else: return 'True'
					elif obj[15]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[9]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=55:
				return 'True'
			else: return 'True'
		elif obj[16]>3.0:
			return 'False'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[17]<=1.0:
			return 'False'
		elif obj[17]>1.0:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
