def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[17]<=2:
		# {"feature": "Time", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]<=0:
					return 'False'
				elif obj[4]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[6]>1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[17]>2:
		# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[5]<=0:
			return 'False'
		elif obj[5]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
