def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 2}
		if obj[7]<=10:
			return 'False'
		elif obj[7]>10:
			# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[8]<=3:
				return 'False'
			elif obj[8]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[4]<=5:
			return 'True'
		elif obj[4]>5:
			return 'False'
		else: return 'False'
	else: return 'True'
