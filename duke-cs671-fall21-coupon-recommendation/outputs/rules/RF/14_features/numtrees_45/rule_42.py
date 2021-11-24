def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]>4:
		# {"feature": "Age", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[4]>0:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[11]<=1.0:
				return 'False'
			elif obj[11]>1.0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=2:
						return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=0:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[7]<=4:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
