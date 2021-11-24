def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]<=1.0:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]>2:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[7]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[8]>1.0:
		# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[9]<=3.0:
				return 'False'
			elif obj[9]>3.0:
				return 'True'
			else: return 'True'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
