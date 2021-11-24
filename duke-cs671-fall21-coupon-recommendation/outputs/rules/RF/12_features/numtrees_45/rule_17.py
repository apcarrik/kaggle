def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]>1:
		# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[4]<=4:
			return 'False'
		elif obj[4]>4:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[0]>0:
			# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[8]>0.0:
				return 'True'
			elif obj[8]<=0.0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>3:
					return 'True'
				elif obj[4]<=3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
