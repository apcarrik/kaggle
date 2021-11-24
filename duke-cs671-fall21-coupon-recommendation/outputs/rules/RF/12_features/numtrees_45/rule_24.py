def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[9]>0.0:
		# {"feature": "Gender", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[3]>0:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[8]<=3.0:
				return 'True'
			elif obj[8]>3.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0:
			# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[8]<=1.0:
				return 'False'
			elif obj[8]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[9]<=0.0:
		return 'False'
	else: return 'False'
