def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]>5:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[10]>0.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>1:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[10]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	elif obj[7]<=5:
		# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[4]>0:
			return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
