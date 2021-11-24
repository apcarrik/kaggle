def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[7]>1:
		# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[13]>1:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]>-1.0:
						return 'False'
					elif obj[11]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[13]<=1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[7]<=1:
		return 'True'
	else: return 'True'
