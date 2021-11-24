def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[6]>0.0:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[8]>1.0:
			# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=2:
				return 'True'
			elif obj[4]>2:
				# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>1:
					return 'False'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]<=1.0:
			# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[3]>0:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4]<=3:
					return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]<=0.0:
		return 'True'
	else: return 'True'
