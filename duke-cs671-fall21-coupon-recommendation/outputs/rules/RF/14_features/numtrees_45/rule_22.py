def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.6292, "depth": 2}
		if obj[7]>4:
			# {"feature": "Income", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[8]<=6:
				return 'True'
			elif obj[8]>6:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>2:
					return 'True'
				elif obj[4]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=4:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[4]>1:
			return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
