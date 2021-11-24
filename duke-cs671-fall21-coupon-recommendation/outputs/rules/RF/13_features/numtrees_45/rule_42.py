def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[6]>1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[7]>1:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[12]>1:
				return 'False'
			elif obj[12]<=1:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=2.0:
					return 'True'
				elif obj[8]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	elif obj[6]<=1:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[7]<=10:
			return 'True'
		elif obj[7]>10:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
