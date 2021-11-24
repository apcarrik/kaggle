def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]<=19:
		# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[4]>1:
			# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[7]>1.0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[10]>1:
						return 'False'
					elif obj[10]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=1.0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]>3:
					return 'False'
				elif obj[2]<=3:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	elif obj[5]>19:
		return 'False'
	else: return 'False'
