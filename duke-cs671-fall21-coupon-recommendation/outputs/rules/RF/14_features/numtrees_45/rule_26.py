def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]>2:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[7]<=10:
			# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[6]>0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[7]>10:
			return 'False'
		else: return 'False'
	elif obj[4]<=2:
		# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
