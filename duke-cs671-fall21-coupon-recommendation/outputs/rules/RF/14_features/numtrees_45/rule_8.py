def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]>1:
		# {"feature": "Time", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]>10:
				return 'False'
			elif obj[7]<=10:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[11]<=2.0:
			return 'False'
		elif obj[11]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
