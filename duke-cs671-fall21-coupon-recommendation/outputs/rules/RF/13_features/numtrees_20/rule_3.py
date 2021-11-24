def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[9]<=3.0:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9996, "depth": 2}
		if obj[7]>1:
			# {"feature": "Time", "instances": 37, "metric_value": 0.974, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Passanger", "instances": 26, "metric_value": 0.8404, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Age", "instances": 18, "metric_value": 0.65, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[6]<=3:
								return 'False'
							elif obj[6]>3:
								return 'True'
							else: return 'True'
						elif obj[8]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[2]>1:
						# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=1.0:
								return 'False'
							elif obj[10]>1.0:
								return 'True'
							else: return 'True'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[2]>3:
					# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2:
								return 'True'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[9]>3.0:
		return 'False'
	else: return 'False'
