def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[9]<=1.0:
		# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>3:
					return 'False'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[9]>1.0:
		# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[4]>0:
			return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
