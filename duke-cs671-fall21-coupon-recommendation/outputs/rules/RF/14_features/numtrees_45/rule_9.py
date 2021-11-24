def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=1.0:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[2]>0:
			# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[4]>1:
				return 'True'
			elif obj[4]<=1:
				# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[11]>1.0:
		# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[2]<=3:
				return 'False'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
