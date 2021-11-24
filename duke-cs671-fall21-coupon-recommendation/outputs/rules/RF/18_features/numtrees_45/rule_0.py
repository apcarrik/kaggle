def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[6]>3:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[13]>1.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[13]<=1.0:
				return 'True'
			else: return 'True'
		elif obj[3]>3:
			return 'False'
		else: return 'False'
	elif obj[6]<=3:
		return 'False'
	else: return 'False'
