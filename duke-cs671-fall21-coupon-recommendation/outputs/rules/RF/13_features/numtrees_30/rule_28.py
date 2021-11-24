def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]>0.0:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[2]>0:
			# {"feature": "Time", "instances": 29, "metric_value": 0.9294, "depth": 3}
			if obj[1]>1:
				# {"feature": "Age", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[7]>6:
						return 'True'
					elif obj[7]<=6:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[7]<=8:
					# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[4]>0:
						# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[6]<=2:
							return 'True'
						elif obj[6]>2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				elif obj[7]>8:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	elif obj[10]<=0.0:
		return 'True'
	else: return 'True'
