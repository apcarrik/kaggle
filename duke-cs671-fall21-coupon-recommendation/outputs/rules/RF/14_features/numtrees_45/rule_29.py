def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>0:
		# {"feature": "Children", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[6]<=1:
				return 'True'
			elif obj[6]>1:
				# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[10]<=2.0:
					return 'False'
				elif obj[10]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>0:
			# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
