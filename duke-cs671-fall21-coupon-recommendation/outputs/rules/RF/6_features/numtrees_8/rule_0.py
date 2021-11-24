def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 88, "metric_value": 0.9024, "depth": 2}
		if obj[3]<=13:
			# {"feature": "Passanger", "instances": 65, "metric_value": 0.8051, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 62, "metric_value": 0.8238, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Education", "instances": 59, "metric_value": 0.8432, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 58, "metric_value": 0.8247, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>13:
			# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 39, "metric_value": 0.8582, "depth": 2}
		if obj[3]<=16:
			# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9082, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Passanger", "instances": 30, "metric_value": 0.9481, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 27, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]>2:
							return 'False'
						elif obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]<=0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[3]>16:
			return 'False'
		else: return 'False'
	else: return 'False'
