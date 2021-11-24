def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[11]>1.0:
		# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 2}
		if obj[7]<=2:
			return 'True'
		elif obj[7]>2:
			# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[5]<=3:
				return 'False'
			elif obj[5]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[11]<=1.0:
		# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[14]>1:
				return 'False'
			elif obj[14]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
