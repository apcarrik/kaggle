def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Gender", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>0:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[6]<=7:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[7]>-1.0:
				return 'True'
			elif obj[7]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[6]>7:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=0:
		# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[4]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
