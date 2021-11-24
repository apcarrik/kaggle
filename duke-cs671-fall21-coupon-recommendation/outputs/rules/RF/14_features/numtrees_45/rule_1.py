def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[8]<=5:
					return 'False'
				elif obj[8]>5:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=2:
						return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>1.0:
				return 'True'
			else: return 'True'
		elif obj[4]>3:
			return 'True'
		else: return 'True'
	elif obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[11]<=2.0:
			return 'True'
		elif obj[11]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'
