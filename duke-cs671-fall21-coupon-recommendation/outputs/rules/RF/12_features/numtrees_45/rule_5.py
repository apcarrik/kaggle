def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[6]>2:
		# {"feature": "Age", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[10]<=0:
					return 'False'
				elif obj[10]>0:
					return 'True'
				else: return 'True'
			elif obj[9]>1.0:
				return 'True'
			else: return 'True'
		elif obj[4]>3:
			# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[10]<=0:
				return 'True'
			elif obj[10]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=2:
		return 'True'
	else: return 'True'
