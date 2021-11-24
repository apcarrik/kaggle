def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[10]<=1.0:
		# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[6]<=1:
			# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[12]>1:
					return 'False'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[6]>1:
			return 'False'
		else: return 'False'
	elif obj[10]>1.0:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[7]>3:
				# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[9]>1.0:
					return 'True'
				elif obj[9]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[7]<=3:
				return 'False'
			else: return 'False'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	else: return 'True'
