def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]<=1.0:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[7]>-1.0:
				return 'False'
			elif obj[7]<=-1.0:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[6]>5:
				return 'True'
			elif obj[6]<=5:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>1.0:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]<=0:
				return 'False'
			elif obj[3]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'